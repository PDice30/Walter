# a note has -> a time, a duration, a pitch
# Should a note have a track/Channel? Where should that be defined?

# If a note is used in a Chord, we only care about the pitch
# All other properties will be defined by the Chord object itself


class Note:

    pitch:      int  # midi pitch class value
    duration:   float  # in beats
    time:       int  # in beats, time in the track when the note actually begins playing
    track:      int
    channel:    int
    volume:     int  # 0 - 127

    #  flags for special note marks
    is_accented: bool
    is_staccato: bool

    def __init__(self, pitch: int, duration = 1, time = 0, track = 0,
                 channel = 0, volume = 100, is_accented = False, is_staccato = False):
        self.pitch = pitch
        self.duration = duration
        self.time = time
        self.track = track
        self.channel = channel
        self.volume = volume
        self.is_accented = is_accented
        self.is_staccato = is_staccato

    # The Note class should have methods that augment it
    # direction is either -1 for lower or 1 for higher
    def move_pitch(self, direction: int, semitones: int):
        self.pitch += (direction * semitones)

    def print_note_pitch(self):
        print('Pitch: ', self.pitch)

    def print_note_all(self):
        print('Pitch: ', self.pitch)
        print('Duration (in beats): ', self.duration)
        print('Time (in beats): ', self.time)
        print('Track: ', self.track)
        print('Channel: ', self.channel)
        print('Volume: ', self.volume)
        print('Accented? : ', self.is_accented)
        print('Staccato? : ', self.is_staccato)

