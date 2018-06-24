from note import Note
from random import Random
from chord import Chord  # This should be an interval/step class


# Difference in Key/Scale?
class Key:
    # what does a key have?
    name_letter:        str  # Letter value of Key
    name_class:         str  # Major/minor
    midi_root:          int  # midi value of root/tonic note
    tonic_pitch:        int  # the root note in which the key is based
    supertonic_pitch:   int  # the 2nd pitch degree
    mediant_pitch:      int  # the 3rd pitch degree
    subdominant_pitch:  int  # the 4th pitch degree
    dominant_pitch:     int  # the 5th pitch degree
    submediant_pitch:   int  # the 6th pitch degree
    leading_pitch:      int  # the 7th pitch degree
    octave_pitch:       int  # the 8th pitch degree

    def __init__(self, name_letter: str, name_class, midi_root: int):
        self.name_letter = name_letter
        self.name_class = name_class
        self.midi_root = midi_root
        self.configure_pitch_values()

    def configure_pitch_values(self):
        if self.name_class == 'Major':
            self.tonic_pitch        = self.midi_root
            self.supertonic_pitch   = self.midi_root + Chord.STEP_Maj2
            self.mediant_pitch      = self.midi_root + Chord.STEP_Maj3
            self.subdominant_pitch  = self.midi_root + Chord.STEP_Perf4
            self.dominant_pitch     = self.midi_root + Chord.STEP_Perf5
            self.submediant_pitch   = self.midi_root + Chord.STEP_Maj6
            self.leading_pitch      = self.midi_root + Chord.STEP_Maj7
            self.octave_pitch       = self.midi_root + Chord.STEP_Perf8
        elif self.name_class == 'Minor':
            self.tonic_pitch        = self.midi_root
            self.supertonic_pitch   = self.midi_root + Chord.STEP_Maj2
            self.mediant_pitch      = self.midi_root + Chord.STEP_Min3
            self.subdominant_pitch  = self.midi_root + Chord.STEP_Perf4
            self.dominant_pitch     = self.midi_root + Chord.STEP_Perf5
            self.submediant_pitch   = self.midi_root + Chord.STEP_Min6
            self.leading_pitch      = self.midi_root + Chord.STEP_Min7
            self.octave_pitch       = self.midi_root + Chord.STEP_Perf8

    def get_random_pitch(self) -> int:
        degree = Random.randint(Random(), 1, 8)

        if degree == 1:
            return self.tonic_pitch
        elif degree == 2:
            return self.supertonic_pitch
        elif degree == 3:
            return self.mediant_pitch
        elif degree == 4:
            return self.subdominant_pitch
        elif degree == 5:
            return self.dominant_pitch
        elif degree == 6:
            return self.subdominant_pitch
        elif degree == 7:
            return self.leading_pitch
        elif degree == 8:
            return self.octave_pitch

    def get_pitch(self, degree: int) -> int:
        if degree == 1:
            return self.tonic_pitch
        elif degree == 2:
            return self.supertonic_pitch
        elif degree == 3:
            return self.mediant_pitch
        elif degree == 4:
            return self.subdominant_pitch
        elif degree == 5:
            return self.dominant_pitch
        elif degree == 6:
            return self.subdominant_pitch
        elif degree == 7:
            return self.leading_pitch
        elif degree == 8:
            return self.octave_pitch
