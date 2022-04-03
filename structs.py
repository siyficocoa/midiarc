class GroundNote:
    def __init__(self, time, track):
        self.time = time
        self.track = track

class MidiNote:
    def __init__(self, note, st_time, end_time, tempo):
        self.note = note
        self.start_time = st_time
        self.end_time = end_time
        self.start_time_ms = int(st_time / 128 / (tempo / 60 / 1000))
        self.ed_time_ms = int(end_time / 128 / (tempo / 60 / 1000))
