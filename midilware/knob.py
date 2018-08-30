import mido


class Knob:
    v = 63

    def __init__(self, in_p, out_p, cc, channel):
        self.in_p = in_p
        self.out_p = out_p
        self.cc = cc
        self.channel = channel

    def handle(self, msg):
        if msg.value == 63:
            print("dec")
            if self.v <= 0:
                self.v = 0
            else:
                self.v -= 1
        elif msg.value == 65:
            print("inc")
            if self.v > 126:
                self.v = 126
            else:
                self.v += 1
