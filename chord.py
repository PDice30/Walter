import copy
from note import Note


class Chord:
    # Should there be a ChordFactory class?
    # What should a 'Chord' have as properties?
    # Notes, Duration.  Should the notes themselves have the duration or the chord itself?

    notes:      list  # of Note objects -- Make this explicit somehow?
    name:       str   # optional chord name
    duration:   int   # n beats
    time:       int   # in beats, time in the track when the note actually begins playing
    track:      int
    channel:    int
    volume:     int   # 0 - 127

    def __init__(self, notes = None, name = '', duration = 1, time = 0, track = 0, channel = 0, volume = 100):
        self.notes = notes
        self.name = name
        self.duration = duration
        self.time = time
        self.track = track
        self.channel = channel
        self.volume = volume

    # base range for notes = 48 (C) to 59 (B)

    # <editor-fold desc="MIDI Pitch Values for Root Notes">
    ROOT_Cb = 47
    ROOT_C  = 48
    ROOT_Cs = 49
    ROOT_Db = 49
    ROOT_D  = 50
    ROOT_Ds = 51
    ROOT_Eb = 51
    ROOT_E  = 52
    ROOT_Es = 53
    ROOT_Fb = 52
    ROOT_F  = 53
    ROOT_Fs = 54
    ROOT_Gb = 54
    ROOT_G  = 55
    ROOT_Gs = 56
    ROOT_Ab = 56
    ROOT_A  = 57
    ROOT_As = 58
    ROOT_Bb = 58
    ROOT_B  = 59
    ROOT_Bs = 60

    ROOT_Note = 0
    # </editor-fold>

    # <editor-fold desc="Interval/Step Values">
    STEP_Min2 = 1
    STEP_Maj2 = 2
    STEP_Min3 = 3
    STEP_Maj3 = 4
    STEP_Perf4 = 5
    STEP_Dim5 = 6
    STEP_Aug4 = 6
    STEP_Perf5 = 7
    STEP_Min6 = 8
    STEP_Maj6 = 9
    STEP_Min7 = 10
    STEP_Maj7 = 11
    STEP_Perf8 = 12
    STEP_Min9 = 13
    STEP_Maj9 = 14
    STEP_Min10 = 15
    STEP_Maj10 = 16
    STEP_Perf11 = 17
    STEP_Dim12 = 18
    STEP_Aug11 = 18
    STEP_Perf12 = 19

    STEP_Octave = 12
    # </editor-fold>

    # There shouldn't be note specifications, it should all be derivable from the input
    # Account for inversions

    # <editor-fold desc="All Chord Values">
    CHORD_Major = [Note(ROOT_Note),
                   Note(ROOT_Note + STEP_Maj3),
                   Note(ROOT_Note + STEP_Perf5)]
    CHORD_Minor = [Note(ROOT_Note),
                   Note(ROOT_Note + STEP_Min3),
                   Note(ROOT_Note + STEP_Perf5)]
    # </editor-fold>

    # CHORD_Major2 = [ROOT_Note, ROOT_Note + STEP_Maj3, ROOT_Note + STEP_Perf5]
    # CHORD_Minor2 = [ROOT_Note, ROOT_Note + STEP_Min3, ROOT_Note + STEP_Perf5]

    C_major     = [ROOT_C, ROOT_C + STEP_Maj3, ROOT_C + STEP_Perf5]
    C_maj7      = [ROOT_C, ROOT_C + STEP_Maj3, ROOT_C + STEP_Perf5, ROOT_C + STEP_Maj7]
    A_minor     = [ROOT_A, ROOT_A + STEP_Min3, ROOT_A + STEP_Perf5]

    # Can this be made more functional for all chords?
    # root should be the midi value of the pitch class

    # <editor-fold desc="Class Functions">

    # needs to be a parent init function before all of this to define the other attributes
    def chord_major(root):
        new_chord = Chord()
        new_chord.notes = Chord.CHORD_Major
        for i, note in enumerate(new_chord.notes):
            new_chord.notes[i].pitch += root
        return new_chord

    def key_translation(step, chord):
        new_chord = copy.copy(chord)
        for i, note in enumerate(chord):
            new_chord.notes[i] = chord.notes[i] + step
        return new_chord

    def chord_minor(root):
        new_chord = Chord()
        new_chord.notes = Chord.CHORD_Minor
        for i, note in enumerate(new_chord.notes):
            new_chord.notes[i].pitch += root
        return new_chord

    def chord_major_doc(root):
        print('Root Note: ', root)
        new_chord = Chord()
        new_chord.notes = Chord.CHORD_Major
        for i, note in enumerate(Chord.CHORD_Major):
            print(i)
            print('Note Object: ', Chord.CHORD_Major[i])
            print('Pitch: ', Chord.CHORD_Major[i].pitch)
        for i, note in enumerate(new_chord.notes):
            print(i)
            print('Note Object: ', new_chord.notes[i])
            print('Pitch: ', new_chord.notes[i].pitch)
        for i, note in enumerate(new_chord.notes):
            new_chord.notes[i].pitch += root
        return new_chord

    # </editor-fold>

    # Print Helper Functions
    def print_notes(self, detailed: bool):
        print('---------- Printing Notes ----------')
        print('Chord Name: ')  # Add the Root Note modded by whatever to find the right note
        if detailed:
            for i, note in enumerate(self.notes):
                Note.print_note_all(self.notes[i])
        else:
            for i, note in enumerate(self.notes):
                Note.print_note_pitch(self.notes[i])
        print('------------------------------------')


