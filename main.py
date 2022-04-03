from structs import GroundNote, MidiNote
import mido


FILE = r"test2.mid"
mid = mido.MidiFile(FILE)
print(f"Tracks:{len(mid.tracks)}")

timeline = 0
midi_message_stack = {60: None, 61: None, 62: None, 63: None}
midi_notes = []
midi_metas = []
messages = []

track = mid.tracks[0]
for message in track:
    if message.type == 'set_tempo':
        midi_metas.append((message.time, message.tempo))

# tempo = midi_metas[0][1]
tempo = 120

for message in track:
    timeline += message.time
    if message.type == "note_on":
        midi_message_stack[message.note] = timeline
    elif message.type == "note_off":
        if (start_time := midi_message_stack[message.note]) is not None:
            midi_notes.append(MidiNote(message.note, start_time, timeline, tempo))
            midi_message_stack[message.note] = None

for note in midi_notes:
    messages.append(f"({note.start_time_ms},{5 - (note.note - 59)});")

audio_offset = 0
beats = 4
meta_message = f"AudioOffset:{audio_offset}\n-\ntiming(0,{tempo},{beats});\n"
format_str = meta_message + "\n".join(messages)
with open("out", "w") as file:
    file.write(format_str)
print(format_str)
