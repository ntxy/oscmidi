import rtmidi


class MidiStuff(object):
    def __init__(self, portindex):
        self.midiout = rtmidi.MidiOut()
        self.available_ports = self.midiout.get_ports()
        self.mapping = {"/ping": 0}

        print("available midi devices:\n", self.available_ports)

        if self.available_ports:
            self.midiout.open_port(0)
            print("selecting index", portindex, ": ",
                  self.midiout.get_ports()[portindex])
        else:
            self.midiout.open_virtual_port("TouchMidi")
            print("open virtual device: TouchMidi")

    def send_message(self, address, *args):
        if address not in self.mapping:
            self.mapping[address] = len(self.mapping)

        control_change = [0xB0, self.mapping[address], args[0] if args else 0]
        self.midiout.send_message(control_change)
        print(address, args, " ==> ", control_change)

    def __del__(self):
        del self.midiout
