from objprint import add_objprint

@add_objprint
class MidiMessage:
    def __init__(self, type, value, time, time_ms):
        self.type = type
        self.value = value
        self.time = time
        self.time_ms = time_ms

@add_objprint
class MidiNote:
    def __init__(self, note, time, time_ms):
        self.note = note
        self.start_time = time[0]
        self.length = time[1] - time[0]
        self.start_time_ms = time_ms[0]
        self.length_ms = time_ms[1] - time_ms[0]
