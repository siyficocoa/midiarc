import sys
import mido
from midi_util import deserializeMidiObj
from chart_util import StringBuilder, mirror
from structs import MidiMessage, MidiNote

KEYMAP = range(60, 64) ## C5 ~ D#5
HOLD_THRESH = 64
#FILE = sys.argv[1]
FILE = r"test2.mid"

mid = mido.MidiFile(FILE)
midi_messages = deserializeMidiObj(mid, KEYMAP, 0)

chart = list()
tempo = 120 
audio_offset = 0
beats = 3
meta_message = f"AudioOffset:{audio_offset}\n-\n"

for message in midi_messages:
    if type(message) is MidiNote:
        if message.length < HOLD_THRESH:
            chart.append(StringBuilder.groundNote(message.start_time_ms, mirror(message.note, KEYMAP[0])))
        else:
            chart.append(StringBuilder.hold(message.start_time_ms, message.start_time_ms + message.length_ms, mirror(message.note, KEYMAP[0])))
    elif type(message) is MidiMessage:
        if message.type == "set_tempo":
            chart.append(StringBuilder.timing(message.time_ms, tempo, beats))

chart_str = meta_message + "\n".join(chart)
# with open("out", "w") as file:
#     file.write(chart_str)
print(chart_str)
