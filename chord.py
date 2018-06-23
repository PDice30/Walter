import copy


class Chord:
    # base range for notes = 48 (C) to 59 (B)

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

    # There shouldn't be note specifications, it should all be derivable from the input
    # Account for inversions
    CHORD_Major = [ROOT_Note, ROOT_Note + STEP_Maj3, ROOT_Note + STEP_Perf5]
    CHORD_Minor = [ROOT_Note, ROOT_Note + STEP_Min3, ROOT_Note + STEP_Perf5]

    C_major     = [ROOT_C, ROOT_C + STEP_Maj3, ROOT_C + STEP_Perf5]
    C_maj7      = [ROOT_C, ROOT_C + STEP_Maj3, ROOT_C + STEP_Perf5, ROOT_C + STEP_Maj7]
    A_minor     = [ROOT_A, ROOT_A + STEP_Min3, ROOT_A + STEP_Perf5]

    def key_translation(self, step, chord):
        new_chord = copy.copy(chord)
        for i, note in enumerate(chord):
            new_chord[i] = chord[i] + step
        return new_chord

    # Can this be made more functional for all chords?
    # root should be the midi value of the pitch class
    def chord_major(self, root):
        new_chord = list(range(len(Chord.CHORD_Major)))
        for i, note in enumerate(Chord.CHORD_Major):
            new_chord[i] = Chord.CHORD_Major[i] + root
        return new_chord

    def chord_minor(self, root):
        new_chord = list(range(len(Chord.CHORD_Minor)))
        for i, note in enumerate(Chord.CHORD_Minor):
            new_chord[i] = Chord.CHORD_Minor[i] + root
        return new_chord