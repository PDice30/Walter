from midiutil.MidiFile import MIDIFile
from chord import Chord
from key import Key
from riff import Riff, MelodicRiff, HarmonicRiff
from note import Note
from argparse import ArgumentParser
from midiutil_extensions import MU_Extensions

# Define an argument in the walter.py call that does detailed or non-detailed notes and make
# the print functions in chord and other places respect that argument

# <editor-fold desc="Command Line Arguments and ArgumentParser Settings">
print_notes_detailed = False
output_filename = ''
# ArgumentParser
parser = ArgumentParser()
parser.add_argument("-d", "--detailed", help = "prints out notes in a detailed format", action = "store_true")
parser.add_argument("-o", "--output_file", help = "specifies the midi output file", type = str)
args = parser.parse_args()
if args.detailed:
    print_notes_detailed = True
if args.output_file:
    output_filename = args.output_file
# </editor-fold>

####### Track Settings #######
track       = 0
channel     = 0
tempo       = 120
time        = 0     # in beats
duration    = 1     # in beats
volume      = 100   # 0  - 127
##############################

####### Test Settings ########
# output_filename = ''

MyMIDI = MIDIFile(2)  # One track, defaults to format 1 (tempo track is created automatically)
MyMIDI.addTempo(track, time, tempo)
MyMIDI.addTrackName(0, time, 'Test Track 0')
MyMIDI.addTrackName(1, time, 'Test Track 1')

# A_Maj_Chord = Chord.chord_major(Chord.ROOT_A, 'A Major', 2, 1)
A_Maj_Chord = Chord.chord_major(Chord.ROOT_A)
# Chord.print_notes(A_Maj_Chord, print_notes_detailed)

A_Maj_Chord.duration = 2
A_Maj_Chord.time = 1

key_A_major = Key('A', 'Major', 57)
key_Cs_minor = Key('Cs', 'Minor', 49)
## Riffs
riff_A_major = MelodicRiff(key_A_major)
riff_A_major.create_riff(16)

riff_Cs_minor = MelodicRiff(key_Cs_minor, [], 1)
riff_Cs_minor.create_riff(16)

# Riff.print_notes(riff_A_major, print_notes_detailed)

MU_Extensions.add_riff(None, MyMIDI, riff_A_major)
MU_Extensions.add_riff(None, MyMIDI, riff_Cs_minor)

with open(output_filename, 'wb') as output_file:
    MyMIDI.writeFile(output_file)


# This method needs to respect the chords stuff!
# MU_Extensions.add_chord(None, MyMIDI, A_Maj_Chord)

# MU_Extensions.addChord()
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
