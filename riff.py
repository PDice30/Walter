# a melodic riff is a series of notes where the next note plays after the duration of the previous note
# there are exceptions of course, but this is the basic melodic riff
from key import Key
from note import Note
from midiutil import MIDIFile
from midiutil_extensions import MU_Extensions
from random import Random


class Riff:

    key: Key
    notes: list
    track: int
    channel: int

    def __init__(self, key: Key):
        self.key = key


class MelodicRiff(Riff):

    def __init__(self, key: Key):
        Riff.__init__(self, key)

    def create_riff(self, midiutil: MIDIFile, num_notes: int, _input = ''):
        time = 0
        for i in range(0, num_notes):
            duration = Random.randint(Random, 1, 4)
            new_pitch = self.key.get_random_pitch()
            self.notes.append(Note(new_pitch, duration, time))
            time += duration

        # divided into sub functions that take in each note and such?
        MU_Extensions.add_riff(MU_Extensions(), midiutil, self)


class HarmonicRiff(Riff):

    def __init__(self, key: Key):
        Riff.__init__(self, key)
