from .knob import Knob
from mido import Message
from mido import open_input
from mido import open_output


class Twister:
    def __init__(self):
        
        self.midi_in = open_input('Midi Fighter Twister')
        self.midi_out = open_output('Midi Fighter Twister')
                
        # four pages of sixteen knobs each
        
        # first two pages are 0x3F/0x41 endless encoders
        # second two pages are 0-127 CCs
        self.controls = [Knob(in_p=self.midi_in, out_p=self.midi_out,
                              cc=c, channel=0) for c in range(32)]
            
    def run(self):
        """Send MIDI CC back to the Twister on the same channel it came
        from. Make it think its encoders are CCs. Keep track of value.
        """
        
        # attach a callback to the port that sends midi back to where
        # it came from!!
        def handler(msg):
            """Process input and send to output"""
            
            # map the income msg to a knob (which maintains value state)
            # so we can output the appropriate # LEDs
            k = self.controls[msg.control]
            k.handle(msg)
            m = Message('control_change', control=msg.control, value=k.v, channel=msg.channel)
            self.midi_out.send(m)
            
        self.midi_in.callback = handler
