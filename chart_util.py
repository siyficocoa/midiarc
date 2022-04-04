class StringBuilder:
    def timing(offset: int, tempo: float, beats: float):
        return f"timing({offset},{tempo:.2f},{beats:.2f});"
    def groundNote(time: int, lane: int):
        return f"({time},{lane});"
    def hold(st_time: int, end_time: int, lane: int):
        return f"hold({st_time},{end_time},{lane});"

def mirror(lane: int, base_note: int):
    return 5 - (lane - (base_note - 1))