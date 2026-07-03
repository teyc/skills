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

## XCUITest harness pattern

Never call `app.launch()`. Instead:
1. Test shells out to `/usr/bin/open <app> --args <flags>` via `Process`.
2. Attach with `XCUIApplication(bundleIdentifier:)` + `activate()`.
3. For relaunch tests (persistence), `app.terminate()` then re-`open`.

## Pass config as `--args`, not `--env`

`open --env VAR=x` is **silently dropped** when the caller is a test
runner. `open <app> --args --my-flag value` always arrives in
`ProcessInfo.processInfo.arguments`. Also: each env var needs its own
`--env` flag — `open --env A=1 B=2` treats `B=2` as a document to open.
Support both in the app (args override env).

## Resolve the app by path, never by bundle ID

`NSWorkspace.urlForApplication(withBundleIdentifier:)` can resolve to a
**stale build** in another DerivedData checkout (parallel worktree builds
each register a copy). In tests, derive the path from the runner:
`Bundle(for: TestClass.self).bundleURL` → up 3 levels (PlugIns → Runner.app
→ Products) → `MyApp.app`.

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

## Misc

- "Timed out while enabling automation mode": first run may fail while
  the TCC grant settles; retry once before diagnosing.
- `log show` needs `--info` for `Logger.info` lines; absence of logs from
  an automation-spawned app proves nothing.
- Verify shutdown scripts with SIGTERM, not SIGINT — background jobs in
  non-interactive shells ignore SIGINT, so your orphan test lies.
- Parallel worktree builds: unregister/delete their DerivedData copies
  when done (`lsregister -u`), or LS keeps offering them.