from structs import *
import mido

def readMidiObj(mid: mido.MidiFile, key_map: list, track_num: int) -> list:
    abs_timeline = 0
    realtime_ms = 0
    midi_message_stacks = {key_map[0]: [],
                        key_map[1]: [],
                        key_map[2]: [],
                        key_map[3]: []}
    midi_messages = []

    track = mid.tracks[track_num]

    # merge NOTE_ON and NOTE_OFF messages to MidiNote objects,
    # and convert relative timeline(which mido uses) to absolute timeline
    # for convenience when converting midi tick to milliseconds
    for index, message in enumerate(track):
        abs_timeline += message.time

        # if current message is a meta message
        if message.type == "set_tempo":
            tempo = round(mido.tempo2bpm(message.tempo))
            realtime_ms += round(message.time / 128 / (tempo / 60 / 1000))
            midi_messages.append(MidiMessage(message.type,
                                            tempo, 
                                            abs_timeline, 
                                            realtime_ms))
            continue

        realtime_ms += round(message.time / 128 / (tempo / 60 / 1000))
        # if current message is a note
        if message.type == "note_on":
            midi_message_stacks[message.note].append((abs_timeline, realtime_ms))
        elif message.type == "note_off":
            if midi_message_stacks[message.note]:
                start_time = midi_message_stacks[message.note].pop(-1)
                midi_messages.append(MidiNote(message.note,
                                            (start_time[0], abs_timeline),
                                            (start_time[1], realtime_ms)))
            else:
                # handle error when popping an empty stack
                # corrupted midi files will cause this error(like a missing NOTE_ON message)
                print("Error: Encountered a NOTE_OFF message with no matching NOTE_ON message, skipped.")
                print(f"at track {track_num}, message {index}:", message)
    return midi_messages