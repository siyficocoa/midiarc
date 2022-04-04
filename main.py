from midi_util import deserializeMidiObj
from structs import MidiNote
import mido

BASE_KEY = 60 #C5
FILE = r"test2.mid"

mid = mido.MidiFile(FILE)
midi_messages = deserializeMidiObj(mid, BASE_KEY)
print(midi_messages)
midi_notes = [message for message in midi_messages if type(message) is MidiNote]

tempo = 120 
messages = []

for note in midi_notes:
    messages.append(f"({note.start_time_ms},{5 - (note.note - 59)});")

audio_offset = 0
beats = 3
meta_message = f"AudioOffset:{audio_offset}\n-\ntiming(0,{tempo:.2f},{beats:.2f});\n"
format_str = meta_message + "\n".join(messages)
# with open("out", "w") as file:
#     file.write(format_str)
print(format_str)
