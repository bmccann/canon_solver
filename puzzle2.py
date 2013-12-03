from music21 import *
c = clef.CClef()
ts = meter.TimeSignature('4/4')
ks = key.KeySignature(0)
s= stream.Stream(cautionaryAll=True, cautionaryPitchClass=True, cautionaryNotImmediateRepeat =True)
puzzle9 = stream.Part()


#Ignore pickups so it's matched more easly
#puzzle9.append(note.Rest(quarterLength=3))
#puzzle9.append(note.Note('C4', quarterLength=0.5))
#puzzle9.append(note.Note('D4', quarterLength=0.5))
puzzle9.append(note.Note('E-4', quarterLength=1))
puzzle9.append(note.Note('E4', quarterLength=1))
puzzle9.append(note.Note('F4', quarterLength=1))
puzzle9.append(note.Note('F#4', quarterLength=1))
puzzle9.append(note.Note('G4', quarterLength=2))
puzzle9.append(note.Note('A-4', quarterLength=2))
puzzle9.append(note.Note('B3', quarterLength=2))
puzzle9.append(note.Rest(quarterLength=1))
puzzle9.append(note.Note('G4', quarterLength=1))
puzzle9.append(note.Note('F#4', quarterLength=1))
puzzle9.append(note.Note('F4', quarterLength=2))
puzzle9.append(note.Note('E4', quarterLength=1))
puzzle9.append(note.Note('E-4', quarterLength=1))
puzzle9.append(note.Note('D4', quarterLength=2))
puzzle9.append(note.Note('C4', quarterLength=1))
puzzle9.append(note.Note('B3', quarterLength=1))
puzzle9.append(note.Note('G3', quarterLength=1))
puzzle9.append(note.Note('C4', quarterLength=1))
puzzle9.append(note.Note('F4', quarterLength=1))
puzzle9.append(note.Note('E-4', quarterLength=2))
puzzle9.append(note.Note('D4', quarterLength=1))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Note('D4', quarterLength=0.5))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Note('C5', quarterLength=0.5))
puzzle9.append(note.Note('B-4', quarterLength=0.5))
puzzle9.append(note.Note('A-4', quarterLength=0.5))
puzzle9.append(note.Note('G4', quarterLength=0.5))
puzzle9.append(note.Note('F4', quarterLength=0.5))
puzzle9.append(note.Note('E-4', quarterLength=0.5))
puzzle9.append(note.Note('G4', quarterLength=0.5))
puzzle9.append(note.Note('F4', quarterLength=0.5))
puzzle9.append(note.Note('G4', quarterLength=0.5))
puzzle9.append(note.Note('F4', quarterLength=0.5))
puzzle9.append(note.Note('E-4', quarterLength=0.5))
puzzle9.append(note.Note('D4', quarterLength=0.5))
puzzle9.append(note.Note('E-4', quarterLength=0.5))
puzzle9.append(note.Note('F4', quarterLength=0.5))
puzzle9.append(note.Note('D4', quarterLength=0.5))
puzzle9.append(note.Note('E-4', quarterLength=0.5))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Note('A3', quarterLength=0.5))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Note('F#3', quarterLength=1))
puzzle9.append(note.Note('G3', quarterLength=0.5))
puzzle9.append(note.Note('A3', quarterLength=0.5))
puzzle9.append(note.Note('B3', quarterLength=0.5))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Note('D4', quarterLength=0.5))
puzzle9.append(note.Note('E-4', quarterLength=0.5))
puzzle9.append(note.Note('F4', quarterLength=1))
puzzle9.append(note.Note('E-4', quarterLength=0.5))
puzzle9.append(note.Note('D4', quarterLength=0.5))
puzzle9.append(note.Note('E-4', quarterLength=0.5))
puzzle9.append(note.Note('D4', quarterLength=0.5))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Note('E-4', quarterLength=0.5))
puzzle9.append(note.Note('D4', quarterLength=1))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Note('B3', quarterLength=0.5))
puzzle9.append(note.Note('C4', quarterLength=1))
puzzle9.append(note.Note('D4', quarterLength=1))
puzzle9.append(note.Note('G3', quarterLength=2))
puzzle9.append(note.Note('F3', quarterLength=2))
puzzle9.append(note.Rest(quarterLength=0.5))
puzzle9.append(note.Note('E-3', quarterLength=0.5))
puzzle9.append(note.Note('F#3', quarterLength=0.5))
puzzle9.append(note.Note('G3', quarterLength=0.5))
puzzle9.append(note.Rest(quarterLength=0.5))
puzzle9.append(note.Note('A3', quarterLength=0.5))
puzzle9.append(note.Note('B3', quarterLength=0.5))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Rest(quarterLength=0.5))
puzzle9.append(note.Note('B3', quarterLength=0.5))
puzzle9.append(note.Note('C4', quarterLength=0.5))
puzzle9.append(note.Note('D4', quarterLength=0.5))


puzzle9.insert(0.0, c)

s.insert(0, puzzle9)
print s.flat.notes[1]
#s.show()

#s.show()
