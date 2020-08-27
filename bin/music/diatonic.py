#CONSTANTS
NOTES = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
DIATONIC_SCALE = [0,2,2,1,2,2,2]
MAJOR_TRIAD = [0,4,3]
MINOR_TRIAD = [0,3,4]
DIM_TRIAD = [0,3,3]

MAJOR_SCALE_CHORDS = ["Major","Minor","Minor","Major","Major","Minor","Diminished"]
DIATONIC_MODES = ["Major","Dorian","Phrygian","Lydian","Mixolydian","Aeolian","Locrian"]
TRIAD = [0,2,2]
SEVENTHS = [0,2,2,2]
SIXTHS = [0,2,2,1]


class Harmony:
  def __init__(self,key):
      self.key = key

    #Get the major scale notes for a given key
  def get_major_scale_notes(self):
      notes = []
      tonic = NOTES.index(self.key)
      note = tonic

      for count, interval in enumerate(DIATONIC_SCALE):
          count += 1
          note = note + interval
          if note > 11:
              note -= 12
          notes.append(NOTES[note])

      return notes

class Chords(Harmony):
    def __init__(self, key):
        super().__init__(key)
        self.key = key
        self.notes = self.get_major_scale_notes()

    def get_triad(self, root = "A"):
        note = self.notes.index(root)

        for c, interval in enumerate(TRIAD):
            note = note + interval
            if note > 6:
                note -= 7
            if c == 0:
                triad = self.notes[note]
            else:
                triad = f'{triad} {self.notes[note]}'
        return triad

    def get_all_triads(self):
        chords = {}
        for c, note in enumerate(self.notes):
            triad = f'{note} {MAJOR_SCALE_CHORDS[c]}'
            if c == 0:
                chord = {"one": {"name": triad, "notes": self.get_triad(root = note)}}
            elif c == 1:
                chord = {"two": {"name": triad, "notes": self.get_triad(root = note)}}        
            elif c == 2:
                chord = {"three": {"name": triad, "notes": self.get_triad(root = note)}}
            elif c == 3:
                chord = {"four": {"name": triad, "notes": self.get_triad(root = note)}} 
            elif c == 4:
                chord = {"five": {"name": triad, "notes": self.get_triad(root = note)}}
            elif c == 5:
                chord = {"six": {"name": triad, "notes": self.get_triad(root = note)}} 
            elif c == 6:
                chord = {"seven": {"name": triad, "notes": self.get_triad(root = note)}}

            chords.update(chord)
        return chords

    def get_all_triads2(self):
        chords = {}
        for c, note in enumerate(self.notes):
            triad = f'{note} {MAJOR_SCALE_CHORDS[c]}'
            chord = {"one": "C E G"}
            chords.update(chord)
        return chords

    def get_seventh(self, root="A"):
        note = self.notes.index(root)
        seventh = []

        for interval in SEVENTHS:
            note = note + interval
            if note > 6:
                note -= 7
            seventh.append(self.notes[note])
        return seventh

    def get_all_sevenths(self):
        MAJOR_SCALE_CHORDS[4] = "Dominant" 
        chords = []
        for c, note in enumerate(self.notes):
            seventh = f'{note} {MAJOR_SCALE_CHORDS[c]} 7'
            if c == 6:
                seventh = f'{note} Half Dim'

            chord = {seventh: self.get_seventh(root = note)}
            chords.append(chord)
        return chords

    def get_diatonic_chords(self):
        diatonic_dict = {self.key: {"triads": self.get_all_triads(), \
                                    "sevenths": self.get_all_sevenths()}}
        return diatonic_dict


def get_all_diatonic_chords():
    all_diatonic_chords = []
    for note in NOTES:
        chords = Chords(note).get_diatonic_chords()
        all_diatonic_chords.append(chords)
    return all_diatonic_chords

def get_all_notes():
    return [{"note":n} for n in NOTES]


        

