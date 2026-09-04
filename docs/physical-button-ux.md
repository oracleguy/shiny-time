# Physical Button UX

The physical interface should stay simple: it supports the common timer actions without becoming a menu system. Complex configuration belongs in the web UI.

## Front buttons

The device has four illuminated front buttons:

| Button | Short press | Hold |
|---|---|---|
| **Favorite 1** | Show its configured date countdown as a temporary overlay | Same action; hold behavior may be extended later |
| **Favorite 2** | Show its configured date countdown as a temporary overlay | Same action; hold behavior may be extended later |
| **+1 minute** | Add 1 minute to the timer | Repeat additions; accelerate over time |
| **Start/Stop** | Contextual start, pause, or resume | Cancel the timer and return to the clock |

### Timer behavior

- From the clock, pressing **+1 minute** enters timer-setting mode and adds one minute.
- While setting a timer, pressing **Start/Stop** begins the countdown.
- Holding **+1 minute** repeats additions quickly. It starts with 1-minute increments, then accelerates to rapid repeats and eventually 5-minute increments, making durations such as 20 or 30 minutes quick to enter.
- While running, **Start/Stop** pauses the timer; pressing it again resumes the countdown.
- While paused, **+1 minute** can add more time.
- Holding **Start/Stop** for about two seconds cancels the timer and returns to the normal clock display. This prevents an accidental short press from destroying a running timer.

## LEDs

Each button has an independently controlled LED. LEDs should communicate the current state at a glance—for example, indicating the active timer state, paused state, or available shortcut—without requiring a menu or text label.

## Favorite buttons and date overlays

Favorite 1 and Favorite 2 initially provide quick access to two configured date countdowns. A date countdown is shown as a temporary overlay, then the display returns to the clock. The Favorite buttons should remain extensible so they can later trigger other configured functions through the web UI.

## Separate Setup button

Use a separate recessed **Setup** button rather than placing setup controls in the everyday front interface. It is reserved for:

- Wi-Fi onboarding and setup mode
- Re-entering or changing device configuration
- Factory reset, using a deliberate long-press sequence

The web UI handles detailed timer, date, favorite, display, and device configuration.
