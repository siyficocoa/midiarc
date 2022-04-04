class GroundNote:
    def __init__(self, time, track):
        self.time = time
        self.track = track

class MidiMessage:
    def __init__(self, type, value, time, time_ms):
        self.type = type
        self.value = value
        self.time = time
        self.time_ms = time_ms

class MidiNote:
    def __init__(self, note, time, time_ms):
        self.note = note
        self.start_time = time[0]
        self.length = time[1] - time[0]
        self.start_time_ms = time_ms[0] #int(st_time / 128 / (tempo / 60 / 1000))
        self.length_ms = time_ms[1] - time_ms[0]

class Stack:
    def __init__(self):
        self.stack = list()
    def put(self, data):
        self.stack.append(data)
    def take(self):
        try:
            ret = self.stack.pop(-1)
        except IndexError:
            return None
        return ret
    def isEmpty(self):
        return False if self.stack else True
