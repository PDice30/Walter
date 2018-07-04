# a melodic riff is a series of notes where the next note plays after the duration of the previous note
# there are exceptions of course, but this is the basic melodic riff
from key import Key
from note import Note
from random import Random

MAX_DURATION = 3
MIN_DURATION = 1


class Riff:

    key: Key
    notes: list  # of Note objects
    track: int
    channel: int

    def __init__(self, key: Key, notes = [], track = 0, channel = 0):
        self.key = key
        self.notes = notes
        self.track = track
        self.channel = channel

        # Print Helper Functions
    def print_notes(self, detailed: bool):
        print('---------- Printing Notes ----------')
        print('Riff Name: ')  # Add the Root Note modded by whatever to find the right note
        if detailed:
            for i, note in enumerate(self.notes):
                Note.print_note_all(self.notes[i])
        else:
            for i, note in enumerate(self.notes):
                Note.print_note_pitch(self.notes[i])
        print('------------------------------------')


class MelodicRiff(Riff):

    def __init__(self, key: Key, notes = [], track = 0, channel = 0):
        Riff.__init__(self, key, notes, track, channel)

    def create_riff(self, riff_length: int, _input = ''):
        time = 0
        while time < riff_length:
            duration = Random.randint(Random(), MIN_DURATION, MAX_DURATION)
            # half a beat
            if duration == 3:
                duration = 0.5
            if duration + time > riff_length:
                continue
            # elif duration == 4:
            #     duration = 0.25
            new_pitch = self.key.get_random_pitch()
            list.append(self.notes, Note(new_pitch, duration, time))
            time += duration


class HarmonicRiff(Riff):

    def __init__(self, key: Key):
        Riff.__init__(self, key)
