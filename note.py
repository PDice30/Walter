# a note has -> a time, a duration, a pitch
# Should a note have a track/Channel? Where should that be defined?

# If a note is used in a Chord, we only care about the pitch
# All other properties will be defined by the Chord object itself


class Note:

    pitch:      int  # midi pitch class value
    duration:   int  # in beats
    time:       int  # in beats, time in the track when the note actually begins playing
    track:      int
    channel:    int
    volume:     int  # 0 - 127

    #  flags for special note marks
    isAccented: bool
    isStaccato: bool

    def __init__(self, pitch: int, duration = 1, time = 0, track = 0,
                 channel = 0, volume = 100, is_accented = False, is_staccato = False):
        self.pitch = pitch
        self.duration = duration
        self.time = time
        self.track = track
        self.channel = channel
        self.volume = volume
        self.isAccented = is_accented
        self.isStaccato = is_staccato

    def print_note_pitch(self):
        print('Pitch: ', self.pitch)

    def print_note_all(self):
        print('Pitch: ', self.pitch)
        print('Duration (in beats): ', self.duration)
        print('Time (in beats): ', self.time)
        print('Track: ', self.track)
        print('Channel: ', self.channel)
        print('Volume: ', self.volume)
        print('Accented? : ', self.isAccented)
        print('Staccato? : ', self.isStaccato)

