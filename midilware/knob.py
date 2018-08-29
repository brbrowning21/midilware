import mido


class Knob:
    v = 63

    def __init__(self, in_p, out_p, cc, channel):
        self.in_p = in_p
        self.out_p = out_p
        self.cc = cc
        self.channel = channel

    def run(self):
        for msg in self.in_p:
            if msg.value == 63:
                if self.v <= 0:
                    self.v = 0
                else:
                    self.v -= 1
            elif msg.value == 65:
                if self.v > 126:
                    self.v = 126
                else:
                    self.v += 1
            self.out_p.send(mido.Message('control_change', control=self.cc, value=self.v, channel=self.channel))
