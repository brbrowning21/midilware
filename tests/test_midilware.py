from queue import Queue


class Knob:
    """
    A knob represents the physical knob and the surrounding LED ring and color
    bar.
    """

    def __init__(self):
        self.value = 0
        self.led_state = 0
        self.color = 0
        self.animation = None


class MockTwister:
    """
    Use this to simulate the physical Midi Fighter Twister for testing. It
    opens up a MIDI port and can be opened with ``mido.open_output()``.
    """

    def __init__(self):
        self.buffer = Queue(1024)
        self.knobs = [Knob() for x in range(16)]

    def change_bank(self, bank_number):
