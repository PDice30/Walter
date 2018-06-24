from note import Note


class Key:
    # what does a key have?
    key: str
    tonic_note:         Note  # the root note in which the key is based
    supertonic_note:    Note  # the 2nd pitch degree
    mediant_note:       Note  # the 3rd pitch degree
    subdominant_note:   Note  # the 4th pitch degree
    dominant_note:      Note  # the 5th pitch degree
    submediant_note:    Note  # the 6th pitch degree
    subtonic_note:      Note  # the 7th pitch degree
    octave_note:        Note  # the 8th pitch degree

    def __init__(self, key: str):
        self.key = key
