Output channels:
0 - # lit of LED bar
  [0, 127]
1 - Color of color bar
  0           - off (set to color of "Off Color" in Midi Fighter Utility)
  [1, 125]    - rainbow
  126, 127    - on
2 - Brightness / animations of color bar and LED ring
  Color bar:
    0         - off
    [1, 8]    - strobe of increasing frequency
    [9, 16]   - glow
    [17, 47]  - dimmest to brightest
    127 - rainbow glow
  LED ring:
    [49, 56]  - strobe
    [57, 64]  - glow
    [65, 95]  - dimmest to brightest
3 - Nothing
4 - Nothing
5 - Animations of the LED ring
  [49, 56]  - strobe
  [57, 64]  - glow
  [65, 95] - dimmest to brightest


Animations can be calculated on the computer and sent via incremental midi
messages. OR they can be optimized and use a premade one that the Twister
offers support from.

When set in ENC 3FH/41H mode, encoder can still keep track of what output
value has been sent to its LED ring.


Input channels
0
1
2
3
4 - When knob is set to "Shift Encoder Hold", turning it while pressed will send
    on this channel
5


Where does buffer live?
Assume it lives within twister
Confirm by connecting Twister to powered usb hub to laptop. Then spamming messages to it, immediately removing USB from hub to laptop. Does the powered Twister still respond to message queue?
Alternative: look at schematic

Test length of buffer (be that internal or external)
Spam with random
Send a known pattern
Start timing
Spam random (count # of these msgs)
Send a known pattern
Stop timing
Idk what this does lol

Random: to prevent midi fighter from optimizing the display updates to LEDs
Known pattern: something to distinguish from random

Another test: try to fill the buffer. After what point does message get lost?

# Test results
Hooked up laptop -> USB hub -> Twister. Spammed messages to Twister, then yanked
the cable between laptop and hub. Twister immediately stopped.
Buffer must live on the laptop side (despite rtmidi library not listing
any buffer/queue on the output side).
This is actually good because it means the MIDI message output rate of the
computer is the bottleneck.
