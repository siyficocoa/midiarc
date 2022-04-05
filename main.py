import sys
import mido
from midi_util import deserializeMidiObj
from chart import midiMessageToChart

KEYMAP = range(60, 64)      ## C5 ~ D#5
HOLD_THRESH = 64            ## midi notes longer than this value will be converted to hold, else a tap
AUDIO_OFFSET = 0

# file = sys.argv[1]
file = r"./testmidi/test2.mid"

mid = mido.MidiFile(file)
midi_messages = deserializeMidiObj(mid, KEYMAP, 0)
chart = midiMessageToChart(midi_messages, HOLD_THRESH, KEYMAP)

meta_message = f"AudioOffset:{AUDIO_OFFSET}\n-\n"
chart_str = meta_message + "\n".join(chart)
# with open("output.aff", "w") as file:
#     file.write(chart_str)
print(chart_str)
