---
name: macos-app-automation
description: Build, launch, screenshot, and E2E-test native macOS apps (SwiftUI/XcodeGen/XCUITest) from an agent or CI shell. Use when building macOS apps, driving XCUITest, capturing app screenshots, or when an app launches but never shows a window under automation.
---

# macOS App Automation — lessons learned the hard way

Hard-won rules for driving native macOS apps from an automation context
(agent shell, CI runner, background session). Discovered on macOS 26 /
Xcode 26; most rules generalize.

## The golden rule: launch via LaunchServices, never posix_spawn

Apps spawned as children of an automation context (agent shell, XCUITest
runner, `launchctl submit`, direct binary exec) run — menu bar and all —
but **never create windows**. TCC "responsible process" inheritance is the
culprit. `/usr/bin/open` disclaims responsibility, so it escapes.

- ✅ `open /path/To.app` — window appears
- ✅ `NSWorkspace.openApplication` *from a normal shell* — works
- ❌ `XCUIApplication.launch()` — windowless app
- ❌ `"$APP/Contents/MacOS/Binary" &` — windowless app
- ❌ `NSWorkspace.openApplication` *from the test runner* — still tainted

## The runner is App-Sandboxed — unconditionally (Xcode 26)

`GlassCRMUITests-Runner.app` carries `com.apple.security.app-sandbox = true`
no matter what; `ENABLE_APP_SANDBOX = NO` on the test target does **not**
remove it (verify: `codesign -d --entitlements - <Runner.app>`). This is the
root cause behind everything the runner "mysteriously" can't do:

- `open --env VAR=x` from the runner: **silently dropped**.
- `open <app> --args --flag` from the runner: **also silently dropped**
  (works fine from a normal shell — do not trust a shell test to validate
  the runner path).
- Files written by the runner (`/tmp/...`): redirected into its container
  (`~/Library/Containers/<runner-id>/Data/...`) — the app never sees them,
  and `FileManager` inside the runner reports success.

## XCUITest harness pattern

Never call `app.launch()`. Instead:
1. Test shells out to `/usr/bin/open <exact-app-path>` via `Process`
   (path-launch first, so the right binary runs).
2. Attach with `XCUIApplication(bundleIdentifier:)`, wait for
   `.runningForeground`, then `activate()`.
3. Deliver test config with a second `open "myapp://test-setup?store=…&reset=1&seed=1"`
   — a **custom URL scheme is the one channel sandboxing permits**. Register
   it in Info.plist (`CFBundleURLTypes`), handle in `.onOpenURL`, wrap the
   handler in `#if DEBUG`. Runtime store swap = hold the `ModelContainer` in
   `@State` and rebuild it in the handler.
4. For relaunch tests (persistence), `app.terminate()` then re-`open`.

Keep `--args`/`--env` parsing in the app anyway — they work from normal
shells and are handy for manual/demo launches (each env var needs its own
`--env` flag; `open --env A=1 B=2` treats `B=2` as a document to open).

## Windows on inactive Spaces are invisible to XCUITest

If the user is in another Space (fullscreen VS Code counts), the AUT's
window exists (`CGWindowList` shows `onscreen=false`) but the AX snapshot
has **no Window element** — queries fail as if the app were windowless.
Test-mode fix in the app (behind the URL-scheme `front=1` flag):

```swift
window.collectionBehavior.insert([.canJoinAllSpaces, .fullScreenAuxiliary])
window.orderFrontRegardless()
NSApp.activate(ignoringOtherApps: true)
```

## Suites need an idle machine

A human typing on the machine contends with XCUITest for keyboard focus and
Spaces: the suite fails with a *different* random subset each run while
every test passes individually — that pattern IS this diagnosis. Gate suite
runs on `HIDIdleTime` ≥ ~3 min:

```bash
ioreg -c IOHIDSystem | awk '/HIDIdleTime/ {print int($NF/1000000000); exit}'
```

Check `pmset -g assertions | grep UserIsActive` to confirm live input.
Side effect of the front-mode fix above: the AUT floats over the user's
fullscreen apps during runs — warn them.

## Resolve the app by path, never by bundle ID

`NSWorkspace.urlForApplication(withBundleIdentifier:)` can resolve to a
**stale build** in another DerivedData checkout (parallel worktree builds
each register a copy — a "passing" run may be exercising outdated code).
In tests, derive the path from the runner bundle: start at
`Bundle(for: TestClass.self).bundleURL` (…/Runner.app/Contents/PlugIns/X.xctest —
note the easy-to-forget `Contents/`) and walk **up one level at a time,
probing for `MyApp.app`** rather than hardcoding a level count. When a
worktree batch is merged, delete its DerivedData and `lsregister -u` its
app copies.

## Screenshots without Screen Recording permission

`screencapture -l<windowid>` fails ("could not create image") without the
TCC grant. Instead: XCTAttachment screenshots inside a UI test
(`lifetime = .keepAlways`), then
`xcrun xcresulttool export attachments --path r.xcresult --output-path dir`
(map names via `manifest.json`). `window.screenshot()` can race right
after launch — `app.screenshot()` is more forgiving.

## XcodeGen gotchas for macOS SwiftUI apps

- Add `INFOPLIST_KEY_NSPrincipalClass: NSApplication` — Xcode's template
  injects it; XcodeGen doesn't. Without it, non-LS launches misbehave.
- Sources are directory-scanned at generate time: new .swift files need
  `xcodegen generate` before they build.
- Consider `ENABLE_DEBUG_DYLIB: NO` — the debug-dylib stub adds launch
  quirks outside Xcode.

## SwiftData test isolation

- Store override flag (`--myapp-store <path>`) + reset flag. On reset,
  delete the `-wal` and `-shm` sidecars too or SQLite resurrects old rows.
- Seed flag (`--myapp-seed`) inserting fixtures when the store is empty —
  gives E2E stable data (e.g. an overdue item) and demo screenshots.
- Call `try context.save()` explicitly after every user mutation. Autosave
  alone loses the last edit when the app is terminated immediately after —
  found by a persistence E2E test (`terminate()` → relaunch → record gone),
  and equally real for a user who quits right after editing.

## Misc

- "Timed out while enabling automation mode": first run may fail while
  the TCC grant settles; retry once before diagnosing.
- `log show` needs `--info` for `Logger.info` lines; absence of logs from
  an automation-spawned app proves nothing.
- Verify shutdown scripts with SIGTERM, not SIGINT — background jobs in
  non-interactive shells ignore SIGINT, so your orphan test lies.
- SwiftUI List rows removed by live filtering can leave a **stale AX node**:
  `element.exists` stays true after the row visually disappears. Assert
  `hittable == false` (or `exists == false OR hittable == false`) for
  filtered-out rows; keep `exists` checks for genuinely deleted records.
- Parallel worktree builds: unregister/delete their DerivedData copies
  when done (`lsregister -u`), or LS keeps offering them.