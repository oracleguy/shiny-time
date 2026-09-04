# Setup Button Requirements

The Setup flow is used rarely and should remain intentionally simple. The four-digit display communicates short status messages and a temporary authorization code; the phone or laptop handles Wi-Fi configuration.

## Entering Setup mode

- Hold the recessed **Setup** button for approximately three seconds.
- Start a temporary, open hotspot with a device-specific SSID such as `Clock-A7F3`.
- Keep the hotspot isolated from the internet and other local devices.
- Generate a new random four-digit authorization code for each Setup session.
- Show the status and code on the four-digit display, alternating when necessary:

```text
SETU → 4827 → SETU → 4827
```

- Use a new code whenever Setup mode begins; do not use a permanent code.
- End Setup mode after successful configuration, cancellation, or approximately ten minutes of inactivity.

The four-digit code confirms that the person configuring the device is physically near it. It is a presence check, not high-security authentication.

## Captive portal flow

1. The user joins the open `Clock-XXXX` hotspot.
2. The setup page opens automatically when captive-portal detection works.
3. If it does not open automatically, the user navigates to `http://192.168.4.1`.
4. The page asks for the four-digit code currently shown on the display.
5. After the code is accepted, the page presents Wi-Fi configuration.
6. The user selects a network, enters its password, and submits the form.
7. The device tests the new connection before leaving Setup mode.

The portal should provide:

- Nearby network list
- SSID, signal strength, and detected security type
- Password field with show/hide control
- Manual entry for hidden networks
- Connection progress and a clear success or failure message

Automatic captive-portal opening is best effort. The direct local address must always be available as a fallback.

## Four-digit display states

Use a small set of short codes that are legible on a seven-segment display:

| Display | Meaning |
|---|---|
| `SETU` | Setup mode is active |
| Four digits | Current authorization code |
| `SCAN` | Scanning for nearby networks |
| `JOIN` | Testing the selected Wi-Fi connection |
| `GOOD` | Wi-Fi connection succeeded |
| `FAIL` | Wi-Fi connection failed |
| `rSEt` | Factory-reset warning or progress |

If a word is not legible on the specific display, use numeric status codes instead.

## Front LED patterns

Assuming single-color LEDs, use simple patterns rather than requiring users to decode colors:

| State | LED pattern |
|---|---|
| Setup ready / waiting for code | All four LEDs gently pulse together |
| Scanning | Slow left-to-right sweep |
| Testing Wi-Fi | Right-to-left sweep |
| Success | All four LEDs flash twice, then turn off |
| Failure | Three short flashes, repeated periodically |
| Factory reset warning | Rapid synchronized flashing |

## Applying Wi-Fi settings

- Do not erase the existing known-good Wi-Fi profile until the replacement connection succeeds.
- Keep the setup hotspot running while the new connection is being tested.
- On success, show `GOOD`, briefly indicate success with the LEDs, then disable the hotspot.
- On failure, show `FAIL`, keep the hotspot running, and return the user to the Wi-Fi form.
- Do not record Wi-Fi passwords in logs or display them after submission.

## Compatibility guidance

The first version should target ordinary home networks:

- WPA2-Personal: supported
- WPA3-Personal: attempt when supported by the Pi’s hardware, firmware, and OS
- WPA2/WPA3 mixed mode: preferred when a router offers it
- Hidden SSIDs: supported through manual entry
- Enterprise / 802.1X networks: out of scope for the initial setup flow
- Networks requiring a browser-based sign-in: out of scope for the initial setup flow

If a WPA3-only connection fails, explain that the user can temporarily enable WPA2/WPA3 mixed mode or WPA2-Personal on the router.

The implementation should use the supported Raspberry Pi OS networking stack and report detected capabilities where practical. The page should not promise WPA3 support universally because behavior can vary by Raspberry Pi model and wireless firmware.

## Factory reset

- Hold the recessed Setup button for approximately ten seconds to begin factory reset.
- Show `rSEt` and use the rapid LED pattern as a warning before completion.
- Factory reset should remove saved Wi-Fi credentials and device configuration only after the hold threshold is reached.