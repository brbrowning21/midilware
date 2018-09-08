"""
This script is for doing some intial stress testing of the Midi Fighter
Twister. I want to see how many messages we can send to it per tick.
"""
from mido import open_input
from mido import open_output
from mido import Message
import datetime

try:

    midi_in = open_input('Midi Fighter Twister')
    midi_out = open_output('Midi Fighter Twister')

    q = midi_in._queue._queue


    def update_all(value):

        for control in range(0, 64):
            m = Message('control_change', control=control, value=value, channel=0)
            midi_out.send(m)

    direction = 1
    v = 0

    start = datetime.datetime.now()
    print("Start: " + str(start))
    iterations = 0

    # Loop through all values and send each
    while True:
        if v == 127:
            direction = -1
        elif v == 0:
            direction = 1
        v += direction

        update_all(v)
        iterations += 1

except KeyboardInterrupt:
    end = datetime.datetime.now()
    print("Ended " + str(end))
    print("Iterations: " + str(iterations))
    print("Average time: " + str((end - start)/iterations))
    midi_out.reset()

# CTRL-C after 10 up-downs of all rings
# they actually stopped spinning at 35.5
# Start: 2018-09-04 09:31:19.938039
# Ended 2018-09-04 09:31:33.203781
# Iterations: 8969
# Average time: 0:00:00.001479

# Iterations AKA send all knobs one value
# 8969 / (128*2) = 35.03 cycles (this fits with what I observed after killing it)

