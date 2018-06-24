from midiutil.MidiFile import MIDIFile
from chord import Chord
from note import Note

class MU_Extensions:

    # Get a reference to the one MyMidi opening?
    # out of order because it makes defaulting easier, should be fine
    def add_chord(self, midiutil: MIDIFile, chord: Chord):
        for i, note in enumerate(chord.notes):
            midiutil.addNote(chord.track, chord.channel, note.pitch, chord.time, chord.duration, chord.volume)

    def add_note(self, midiutil: MIDIFile, note: Note):
        midiutil.addNote(note.track, note.channel, note.pitch, note.time, note.duration, note.volume)
