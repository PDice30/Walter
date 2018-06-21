from midiutil.MidiFile import MIDIFile

myMidi = MIDIFile(1)

time = 0
track = 0

myMidi.addTrackName(track, time, 'Sample Track 2')
myMidi.addTempo(track, time, 120)

track = 0
channel = 0
pitch = 60
time = 0
duration = 1
volume = 100

myMidi.addNote(track, channel, pitch, time, duration, volume)

binfile = open('output.mid', 'wb')
myMidi.writeFile(binfile)
binfile.close()