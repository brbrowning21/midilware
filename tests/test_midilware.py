from queue import Queue


class Knob:


class MockTwister:
    """
    Use this to simulate the physical Midi Fighter Twister for testing. It
    opens up a MIDI port and can be opened with ``mido.open_output()``.
    """

    def __init__(self):
        self.buffer = Queue(1024)
        self.knobs =