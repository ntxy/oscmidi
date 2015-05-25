## OSC to MIDI Bridge

Recieves OSC and sends control change MIDI.
Intended as simple solution for TouchOSC on Linux.

    

* The first MIDI byte is always 'control change' 176 or 0xB0.

* OSC addresses are uniquely mapped to the second MIDI byte. This can be done on the fly or from a mapping file. The mapping is written to disk when the program exits. '/ping' is always mapped to 0.

* The third byte is the first value of the OSC message multiplied by 127 and rounded.


### Installation

    > pip install -r requirements.txt
    
### Usage

    usage: oscmidi.py [-h] [--ip IP] [--port PORT] [--midi MIDI]
                    [--mapping-file-in MAPPING_FILE_IN]
                    [--mapping-file-out MAPPING_FILE_OUT] [--no-learn]

    optional arguments:
        -h, --help          show this help message and exit
        --ip IP             The ip to listen on (default=0.0.0.0)
        --port PORT         The port to listen on (default=5005)
        --midi MIDI         The MIDI device index (default=0)
        --mapping-file-in MAPPING_FILE_IN
                            File to read for the OSC to MIDI mapping (default=mapping.json)
        --mapping-file-out MAPPING_FILE_OUT
                            File for saving the mapping (default=mapping.json)
        --no-learn            Map new OSC paths to MIDI

