from note import Note


class Arpeggio:

    notes:      list  # of Note objects -- Make this explicit somehow?
    duration:   float
    time:       int  # in beats, time in the track when the note actually begins playing
    track:      int
    channel:    int
    volume:     int  # 0 - 127

    def __init__(self, notes = None, duration = 1, time = 0, track = 0, channel = 0, volume = 100):
        self.notes = notes
        self.duration = duration
        self.time = time
        self.track = track
        self.channel = channel
        self.volume = volume


