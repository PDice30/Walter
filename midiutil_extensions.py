from midiutil.MidiFile import MIDIFile
class MU_Extensions:

    # Get a reference to the one MyMidi opening?
    # out of order because it makes defaulting easier, should be fine
    def addChord(self, midiutil, chord, time = 0, duration = 1, track = 0, channel= 0, volume = 100):
        for i, note in enumerate(chord):
            midiutil.addNote(track, channel, note, time, duration, volume)
