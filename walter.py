from midiutil.MidiFile import MIDIFile
from chord import Chord
from midiutil_extensions import MU_Extensions

# Define an argument in the walter.py call that does detailed or non-detailed notes and make
# the print functions in chord and other places respect that argument


####### Track Settings #######
track       = 0
channel     = 0
tempo       = 180
time        = 0     # in beats
duration    = 1     # in beats
volume      = 100   # 0  - 127
##############################

####### Test Settings ########
output_filename = 'chord-tests02.mid'

MyMIDI = MIDIFile(2)  # One track, defaults to format 1 (tempo track is created automatically)
MyMIDI.addTempo(track, time, tempo)
MyMIDI.addTrackName(track, time, 'Test Track 1')

# B_Major_Chord = Chord.chord_major(None, Chord.ROOT_B)
# Cs_Minor_Chord = Chord.chord_minor(None, Chord.ROOT_Cs)
#
# print(B_Major_Chord)
# print(Cs_Minor_Chord)

A_Maj_Chord = Chord.chord_major(None, Chord.ROOT_A)
Chord.print_notes_pitch(A_Maj_Chord)

# Make a better extension method to get rid of this ugliness
#
# for i in range(0, 13):
#     MU_Extensions.addChord(None,
#                            MyMIDI,
#                            Chord.key_translation(None, i, Chord.chord_major(None, Chord.ROOT_E - Chord.STEP_Octave)),
#                            time + (i * 2),
#                            duration,
#                            0)
#
# for i in range(0, 13):
#     MU_Extensions.addChord(None,
#                            MyMIDI,
#                            Chord.key_translation(None, i, Chord.chord_major(None, Chord.ROOT_Gs - Chord.STEP_Octave)),
#                            time + (i * 2),
#                            duration,
#                            1)


with open(output_filename, 'wb') as output_file:
    MyMIDI.writeFile(output_file)


# print(notesC)
# notesD = Chord.key_translation(None, 2, notesC)
# print(notesD)

# print(C_Major_Chord)
# D_Major_Chord = Chord.key_translation(None, 2, C_Major_Chord)
# print(D_Major_Chord)
# print(C_Major_Chord)
#
# for i, pitch in enumerate(notesC):
#     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
# for i, pitch in enumerate(notesE):
#     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
# for i, pitch in enumerate(notesG):
#     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
