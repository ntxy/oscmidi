import argparse

from pythonosc import dispatcher
from pythonosc import osc_server

import send_midi


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="0.0.0.0", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  parser.add_argument("--midi",
      type=int, default=0, help="The MIDI device index")
  args = parser.parse_args()

  midistuff = send_midi.MidiStuff(args.midi)

  dispatcher = dispatcher.Dispatcher()
  dispatcher.set_default_handler(midistuff.send_message)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving OSC on {}".format(server.server_address))
  server.serve_forever()
