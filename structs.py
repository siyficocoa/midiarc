class MidiMessage:
    def __init__(self, type, value, time, time_ms):
        self.type = type
        self.value = value
        self.time = time
        self.time_ms = time_ms
    def __str__(self):
        head = f"<MidiMessage object at {str(hex(id(self)))}:"
        body = f"<type:{self.type}, value:{self.value}, time:{self.time}, time_ms:{self.time_ms}>"
        return head + body + ">"


class MidiNote:
    def __init__(self, note, time, time_ms):
        self.note = note
        self.start_time = time[0]
        self.length = time[1] - time[0]
        self.start_time_ms = time_ms[0]
        self.length_ms = time_ms[1] - time_ms[0]
    def __str__(self):
        head = f"<MidiMessage object at {str(hex(id(self)))}:"
        body = f"<note:{self.note}, start_time:{self.start_time}, length:{self.length}, start_time_ms:{self.start_time_ms}, length_ms:{self.length_ms}>"
        return head + body + ">"
