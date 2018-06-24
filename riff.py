# a melodic riff is a series of notes where the next note plays after the duration of the previous note
# there are exceptions of course, but this is the basic melodic riff
from key import Key


class Riff:

    key: Key

    def __init__(self, key: Key):
        self.key = key


class MelodicRiff(Riff):

    notes: list  # list of Note objects

    def __init__(self, key: Key):
        Riff.__init__(self, key)

    def create_riff(self, key: Key):

        # divided into sub functions that take in each note and such?




class HarmonicRiff(Riff):

    def __init__(self, key: Key):
        Riff.__init__(self, key)
