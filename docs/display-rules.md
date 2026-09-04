# Display Rules

The device uses a four-digit seven-segment display. The display should show one clear state at a time and avoid trying to present complex configuration.

## Display precedence

The highest applicable priority wins:

1. Factory-reset confirmation
2. Wi-Fi Setup mode
3. Timer-finished alert
4. Active timer
5. Favorite date overlay
6. Normal clock

A higher-priority state blocks lower-priority overlays. Only one temporary message may be active at a time.

## Default clock

When no higher-priority state is active, display local time as `HH:MM`.

## Timer display

- Timers with less than 100 minutes remaining display `MM:SS`.
- Timers with 100 minutes or more remaining display `HH:MM`.
- A long timer switches to `MM:SS` once it drops below 100 minutes, so the display becomes more precise near completion.
- The maximum timer value is 99 hours and 59 minutes.

Example:

```text
01:40  hours:minutes
99:59  minutes:seconds
```

## Favorite date overlays

- Favorite 1 and Favorite 2 show their configured date countdown as a temporary overlay.
- Date countdowns display whole calendar days only, without hours or minutes.
- On December 24, a Christmas countdown displays `1` at any time of day.
- At any time on December 25, it displays `0`.
- Recurring dates roll forward to their next occurrence.
- The overlay automatically returns to the clock after a few seconds.
- Favorite overlays do not hide an active or paused timer.

## Status messages

Use short seven-segment-friendly codes where the display can render them clearly:

| Display | Meaning |
|---|---|
| `SETU` | Setup mode active |
| Four digits | Setup authorization code |
| `SCAN` | Scanning for Wi-Fi networks |
| `JOIN` | Testing the selected Wi-Fi connection |
| `GOOD` | Wi-Fi connection succeeded |
| `FAIL` | Wi-Fi connection failed |
| `DONE` | Timer finished |
| `rSEt` | Factory-reset warning or progress |

If a word is not legible on the specific display, use a numeric status code instead.

## Timer-finished alert

When a timer reaches zero:

- Display `DONE`.
- Use the timer-alert LED pattern.
- Keep the alert visible briefly, then return to the clock.
- Continue a less intrusive LED reminder until any front-button press acknowledges it.
