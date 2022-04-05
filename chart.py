from structs import MidiNote, MidiMessage

class StringBuilder:
    def timing(offset: int, tempo: float, beats: float):
        return f"timing({offset},{tempo:.2f},{beats:.2f});"
    def groundNote(time: int, lane: int):
        return f"({time},{lane});"
    def hold(st_time: int, end_time: int, lane: int):
        return f"hold({st_time},{end_time},{lane});"

def mirror(lane: int, base_note: int):
    return 5 - (lane - (base_note - 1))

def midiMessageToChart(messages: list, hold_thresh: int, keymap: list, beats=4) -> list[str]:
    ret = list()
    for message in messages:
        if type(message) is MidiNote:
            if message.length < hold_thresh:
                ret.append(StringBuilder.groundNote(message.start_time_ms, mirror(message.note, keymap[0])))
            else:
                ret.append(StringBuilder.hold(message.start_time_ms, message.start_time_ms + message.length_ms, mirror(message.note, keymap[0])))
        elif type(message) is MidiMessage:
            if message.type == "set_tempo":
                ret.append(StringBuilder.timing(message.time_ms, message.value, beats))
    return ret