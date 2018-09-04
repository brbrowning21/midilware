from mido import *
from mido import open_input
from mido import open_output
from mido import Message

midi_in = open_input('Midi Fighter Twister')
midi_out = open_output('Midi Fighter Twister')

# Use knobs as input to learn how outputs are mapped on one knob

control = 0
value = 0
channel = 0

print(dir(midi_in))

for msg in midi_in:
    
    if msg.control == 32:
        control = msg.value
    elif msg.control == 33:
        value = msg.value
    elif msg.control == 34:
        channel = msg.value % 16

    m = Message('control_change', control=control, value=value, channel=channel)
    print(m)
    midi_out.send(m)

print("Done")
