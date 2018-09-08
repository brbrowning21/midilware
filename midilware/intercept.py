from mido import open_input
from mido import open_output
from mido import Message

midi_in = open_input('Midi Fighter Twister')
midi_out = open_output('midilware', virtual=True)

for msg in midi_in:
    midi_out.send(msg)
