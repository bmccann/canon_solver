from music21 import *
c1 = clef.TrebleClef()
row = stream.Stream()
dottedQuarter = duration.Duration(type = 'quarter', dots = 1)
row.append(note.Note('D4', quarterLength=1.5))
row.append(note.Note('D4', quarterLength=1.5)) 

row.append(note.Note('D4', quarterLength=1)) 
row.append(note.Note('E4', quarterLength=0.5)) 
row.append(note.Note('F#4', quarterLength=1.5)) 

row.append(note.Note('F#4', quarterLength=1)) 
row.append(note.Note('E4', quarterLength=0.5)) 
row.append(note.Note('F#4', quarterLength=1)) 
row.append(note.Note('G4', quarterLength=0.5))

row.append(note.Note('A4', quarterLength=3)) 

row.append(note.Note('D5', quarterLength=0.5))
row.append(note.Note('D5', quarterLength=0.5)) 
row.append(note.Note('D5', quarterLength=0.5)) 
row.append(note.Note('A4', quarterLength=0.5)) 
row.append(note.Note('A4', quarterLength=0.5)) 
row.append(note.Note('A4', quarterLength=0.5)) 

row.append(note.Note('F#4', quarterLength=0.5))
row.append(note.Note('F#4', quarterLength=0.5)) 
row.append(note.Note('F#4', quarterLength=0.5)) 
row.append(note.Note('D4', quarterLength=0.5)) 
row.append(note.Note('D4', quarterLength=0.5)) 
row.append(note.Note('D4', quarterLength=0.5)) 

row.append(note.Note('A4', quarterLength=1))
row.append(note.Note('G4', quarterLength=0.5))
row.append(note.Note('F#4', quarterLength=1))
row.append(note.Note('E4', quarterLength=0.5))

row.append(note.Note('D4', quarterLength=3)) 

row.show()

