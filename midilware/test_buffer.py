"""
This script is for doing some intial stress testing of the Midi Fighter
Twister. I want to see how many messages we can send to it per tick.
"""
from mido import open_input
from mido import open_output
from mido import Message


midi_in = open_input('Midi Fighter Twister')
midi_out = open_output('Midi Fighter Twister')

def update_all(value):

    for control in range(0, 64):
        m = Message('control_change', control=control, value=value, channel=0)
        midi_out.send(m)

direction = 1
v = 0

# Loop through all values and send each
while True:
    if v == 127:
        direction = -1
    elif v == 0:
        direction = 1
    v += direction

    update_all(v)
