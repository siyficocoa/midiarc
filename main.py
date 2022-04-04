from midi_util import deserializeMidiObj
from structs import MidiNote, MidiMessage
import mido
import sys

BASE_KEY = range(60, 64) ## C5 ~ D#5
HOLD_THRESH = 64
FILE = sys.argv[1]
# FILE = r"test2.mid"

mid = mido.MidiFile(FILE)
midi_messages = deserializeMidiObj(mid, BASE_KEY, 0)

chart = list()
tempo = 120 
audio_offset = -775
beats = 3
meta_message = f"AudioOffset:{audio_offset}\n-\n"

for message in midi_messages:
    if type(message) is MidiNote:
        chart.append(f"({message.start_time_ms},{5 - (message.note - 59)});")
    elif type(message) is MidiMessage:
        if message.type == "set_tempo":
            chart.append(f"timing(0,{tempo:.2f},{beats:.2f});")

chart_str = meta_message + "\n".join(chart)
# with open("out", "w") as file:
#     file.write(chart_str)
print(chart_str)
