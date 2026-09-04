# Timer Requirements

The physical timer should make common countdowns quick to create without turning the clock into a menu-driven controller. Detailed or unusual timer configuration belongs in the web UI.

## Timer states

- **Idle:** The normal clock is displayed.
- **Setting:** The user is choosing a duration.
- **Running:** The countdown is active.
- **Paused:** The countdown is stopped but can resume.
- **Finished:** The timer has reached zero and requires acknowledgement.

## Physical controls

### +1 minute

- Short press from Idle: enter timer-setting mode and add one minute.
- Short press while Setting or Paused: add one minute.
- Hold: repeat additions automatically.
- Repetition begins with one-minute increments, accelerates over time, and may switch to five-minute increments for rapidly entering longer durations.

### Start/Stop

- Short press while Setting: start the countdown.
- Short press while Running: pause the countdown.
- Short press while Paused: resume the countdown.
- Hold for approximately two seconds: cancel the timer and return to the clock.

## Timer limits and display format

- The maximum physical timer duration is 99 hours and 59 minutes.
- Below 100 minutes remaining, display minutes and seconds as `MM:SS`.
- At 100 minutes or more remaining, display hours and minutes as `HH:MM`.
- A long timer switches to `MM:SS` when it drops below 100 minutes.

Example:

```text
02:00  hours:minutes
01:40  hours:minutes
99:59  minutes:seconds
00:12  minutes:seconds
```

## Completion

- At zero, enter the Finished state and display `DONE`.
- The timer-finished alert should be visible briefly and use a distinct LED pattern.
- Any front-button press acknowledges the alert and returns to the clock.

## Interaction boundaries

- Favorite date overlays must not hide a Running or Paused timer.
- Setup mode takes precedence over the timer display.
- The timer continues running only when its state is Running; entering Setup should not silently change the timer state unless explicitly specified by the implementation.
- The web UI may support more advanced timer configuration, but the physical controls should remain limited to the simple flow above.
