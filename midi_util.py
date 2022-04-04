from structs import *
import mido

def deserializeMidiObj(mid: mido.MidiFile, key_map: list, track_num: int) -> list:
    print(f"Tracks:{len(mid.tracks)}")

    abs_timeline = 0
    realtime_ms = 0
    midi_message_stack = {key_map[0]: Stack(),
                        key_map[1]: Stack(),
                        key_map[2]: Stack(),
                        key_map[3]: Stack()}
    midi_messages = []

    track = mid.tracks[track_num]

    for message in track:
        abs_timeline += message.time
        if message.type == "set_tempo":
            tempo = int(mido.tempo2bpm(message.tempo))
            realtime_ms += int(message.time / 128 / (tempo / 60 / 1000))
            midi_messages.append(MidiMessage(message.type, tempo, abs_timeline, realtime_ms))
            continue
        realtime_ms += int(message.time / 128 / (tempo / 60 / 1000))
        if message.type == "note_on":
            midi_message_stack[message.note].put((abs_timeline, realtime_ms))
        elif message.type == "note_off":
            if not midi_message_stack[message.note].isEmpty():
                start_time = midi_message_stack[message.note].take()
                midi_messages.append(MidiNote(message.note, (start_time[0], abs_timeline), (start_time[1], realtime_ms)))
    return midi_messages
