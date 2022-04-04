from structs import MidiNote, MidiMessage
import mido

def deserializeMidiObj(mid: mido.MidiFile, key_map: int):
    print(f"Tracks:{len(mid.tracks)}")

    abs_timeline = 0
    midi_message_stack = {key_map: None,
                        key_map + 1: None,
                        key_map + 2: None,
                        key_map + 3: None}
    midi_messages = []

    track = mid.tracks[0]

    for message in track:
        abs_timeline += message.time
        if message.type == "set_tempo":
            tempo = 220
            midi_messages.append(MidiMessage(message.type, message.tempo, abs_timeline, tempo))
        elif message.type == "note_on":
            midi_message_stack[message.note] = abs_timeline
        elif message.type == "note_off":
            if (start_time := midi_message_stack[message.note]) is not None:
                midi_messages.append(MidiNote(message.note, start_time, abs_timeline, tempo))
                midi_message_stack[message.note] = None

    return midi_messages
