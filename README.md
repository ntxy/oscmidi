## TouchOSC to MIDI Bridge

Recieves OSC and sends control change MIDI.
Intended as simple solution for TouchOSC on Linux.

    

* The first MIDI byte is always 'control change' 176 or 0xB0.

* OSC addresses are uniquely mapped to the second MIDI byte.
This is done on the fly as OSC messages are recieved. To get consistent mappings you have to trigger the controls in the same order. '/ping' is always mapped to 0.

* The third byte is the first value of the OSC message multiplied by 127 and rounded.


explodes if u use more than 127 different controls in TouchOSC.

### Installation

    > pip install -r requirements.txt
    
### Usage

    > python touchmidi.py [-h] [--ip IP] [--port PORT] [--midi MIDI]
    
    optional arguments:
      -h, --help   show this help message and exit
      --ip IP      The ip to listen on
      --port PORT  The port to listen on
      --midi MIDI  The MIDI device index

