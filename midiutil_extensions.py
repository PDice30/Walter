from midiutil.MidiFile import MIDIFile
from chord import Chord
from note import Note


class MU_Extensions:

    # Get a reference to the one MyMidi opening?
    # out of order because it makes defaulting easier, should be fine
    def addChord(self, midiutil, chord: Chord, time = 0, duration = 1, track = 0, channel= 0, volume = 100):
        for note in enumerate(chord.notes):
            midiutil.addNote(track, channel, note.pitch, time, duration, volume)

    def addNote(self, midiutil, note: Note):
        midiutil.addNote(note.track, note.channel, note.pitch, note.time, note.duration, note.volume)
