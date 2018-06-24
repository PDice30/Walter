from midiutil import MIDIFile
from chord import Chord
from note import Note
from riff import Riff, MelodicRiff, HarmonicRiff


class MU_Extensions:

    # Get a reference to the one MyMidi opening?
    # out of order because it makes defaulting easier, should be fine
    def add_chord(self, midiutil: MIDIFile, chord: Chord):
        for i, note in enumerate(chord.notes):
            midiutil.addNote(chord.track, chord.channel, note.pitch, chord.time, chord.duration, chord.volume)

    def add_note(self, midiutil: MIDIFile, note: Note):
        midiutil.addNote(note.track, note.channel, note.pitch, note.time, note.duration, note.volume)

    # def add_notes

    def add_riff(self, midiutil: MIDIFile, riff: Riff):
        for i, note in enumerate(riff.notes):
            midiutil.addNote(riff.track, riff.channel, riff.notes[i].pitch,
                             riff.notes[i].time, riff.notes[i].duration, riff.notes[i].volume)
