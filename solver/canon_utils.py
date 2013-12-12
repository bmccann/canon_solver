import math
from music21 import *


def getCosts(specifier):
	if specifier == "simple":
			return {0:0, 5:0, 7:0, 9:.2, 4:.2, 3:.2, 8:.2, 1:.4, 2:.4, 6:.4, 10:.4, 11:.4}

def getSimpleCosts():
	return getCosts("simple")

def getNotes(specifier):
	if specifier == "simple":
		  return {"C" : 0, "D" : 2, "E" : 4, "F" : 5, "G" : 7, "A" : 9, "B" :11}
	else:
	  return {}

def getSimpleNotes():
	return getNotes("simple")

def incrementSparseVector(v1, scale, v2):
  """ 
  Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
  """
  for key in set(v1.keys()).union(set(v2.keys())):
      v1[key] += scale * v2[key] 

def euclideanDistance(v1, v2):
	sum_squares = 0
	for key in set(v1.keys()).union(set(v2.keys())):
		sum_squares += (float(v1[key]) - float(v2[key]))**2
	return math.sqrt(sum_squares)

def puzzle1():
	c = clef.SopranoClef()
	ts = meter.TimeSignature('4/4')
	ks = key.KeySignature(-3)
	s= stream.Stream(cautionaryAll=True, cautionaryPitchClass=True, cautionaryNotImmediateRepeat =True)
	puzzle1 = stream.Part()
	puzzle1.insert(0.0, c)

	puzzle1.insert(0.0, ts)
	puzzle1.insert(0.0, ks)

	#ignore pickups for now
	puzzle1.append(note.Note('C4', quarterLength=2))
	puzzle1.append(note.Note('E-4', quarterLength=2))

	puzzle1.append(note.Note('G4', quarterLength=2))
	puzzle1.append(note.Note('A-4', quarterLength=2))

	puzzle1.append(note.Note('B3', quarterLength=2))
	puzzle1.append(note.Rest())
	puzzle1.append(note.Note('G4', quarterLength=2))
	puzzle1.append(note.Note('F#4', quarterLength=2))
	puzzle1.append(note.Note('F4', quarterLength=2))
	puzzle1.append(note.Note('E4', quarterLength=2))
	puzzle1.append(note.Note('E-4', quarterLength=2))

	puzzle1.append(note.Note('D4', quarterLength=1))
	puzzle1.append(note.Note('D-4', quarterLength=1))
	puzzle1.append(note.Note('C4', quarterLength=1))

	puzzle1.append(note.Note('B3', quarterLength=1))
	puzzle1.append(note.Note('G3', quarterLength=1))
	puzzle1.append(note.Note('C4', quarterLength=1))
	puzzle1.append(note.Note('F4', quarterLength=1))

	puzzle1.append(note.Note('E-4', quarterLength=2))
	puzzle1.append(note.Note('D4', quarterLength=2))

	puzzle1.append(note.Note('C4', quarterLength=2))
	puzzle1.append(note.Note('E-4', quarterLength=2))

	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('F4', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('C5', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('E-4', quarterLength=0.5))
	puzzle1.append(note.Note('D4', quarterLength=0.5))
	puzzle1.append(note.Note('E-4', quarterLength=0.5))

	puzzle1.append(note.Note('F4', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('A4', quarterLength=0.5))
	puzzle1.append(note.Note('B4', quarterLength=0.5))
	puzzle1.append(note.Note('C5', quarterLength=0.5))
	puzzle1.append(note.Note('E-4', quarterLength=0.5))
	puzzle1.append(note.Note('F4', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))

	puzzle1.append(note.Note('A-4', quarterLength=0.5))
	puzzle1.append(note.Note('D4', quarterLength=0.5))
	puzzle1.append(note.Note('E-4', quarterLength=0.5))
	puzzle1.append(note.Note('F4', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('F4', quarterLength=0.5))
	puzzle1.append(note.Note('E-4', quarterLength=0.5))
	puzzle1.append(note.Note('D4', quarterLength=0.5))

	puzzle1.append(note.Note('E-4', quarterLength=0.5))
	puzzle1.append(note.Note('F4', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('A-4', quarterLength=0.5))
	puzzle1.append(note.Note('B-4', quarterLength=0.5))
	puzzle1.append(note.Note('A-4', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('F4', quarterLength=0.5))

	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('A-4', quarterLength=0.5))
	puzzle1.append(note.Note('B-4', quarterLength=0.5))
	puzzle1.append(note.Note('C5', quarterLength=0.5))
	puzzle1.append(note.Note('D-5', quarterLength=0.5))
	puzzle1.append(note.Note('B-4', quarterLength=0.5))
	puzzle1.append(note.Note('A-4', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))

	puzzle1.append(note.Note('A4', quarterLength=0.5))
	puzzle1.append(note.Note('B4', quarterLength=0.5))
	puzzle1.append(note.Note('C5', quarterLength=0.5))
	puzzle1.append(note.Note('D5', quarterLength=0.5))
	puzzle1.append(note.Note('E-5', quarterLength=0.5))
	puzzle1.append(note.Note('C5', quarterLength=0.5))
	puzzle1.append(note.Note('B4', quarterLength=0.5))
	puzzle1.append(note.Note('A4', quarterLength=0.5))

	puzzle1.append(note.Note('B4', quarterLength=0.5))
	puzzle1.append(note.Note('C5', quarterLength=0.5))
	puzzle1.append(note.Note('D5', quarterLength=0.5))
	puzzle1.append(note.Note('E-5', quarterLength=0.5))
	puzzle1.append(note.Note('F5', quarterLength=0.5))
	puzzle1.append(note.Note('D5', quarterLength=0.5))
	puzzle1.append(note.Note('G4', quarterLength=0.5))
	puzzle1.append(note.Note('D5', quarterLength=0.5))

	puzzle1.append(note.Note('C5', quarterLength=0.5))
	puzzle1.append(note.Note('D5', quarterLength=0.5))
	puzzle1.append(note.Note('E-5', quarterLength=0.5))
	puzzle1.append(note.Note('F5', quarterLength=0.5))
	puzzle1.append(note.Note('E-5', quarterLength=0.5))
	puzzle1.append(note.Note('D5', quarterLength=0.5))
	puzzle1.append(note.Note('C5', quarterLength=0.5))
	puzzle1.append(note.Note('B4', quarterLength=0.5))

	puzzle1.append(note.Note('C5', quarterLength=1))
	puzzle1.append(note.Note('G4', quarterLength=1))
	puzzle1.append(note.Note('E-4', quarterLength=1))
	puzzle1.append(note.Note('C4', quarterLength=1))


	part2 = stream.Part()
	part2.insert(0.0, c)
	part2.insert(0.0, ts)
	part2.insert(0.0, ks)


	part2.append(note.Note('C4', quarterLength=1))
	part2.append(note.Note('E-4', quarterLength=1))
	part2.append(note.Note('G4', quarterLength=1))
	part2.append(note.Note('C5', quarterLength=1))

	part2.append(note.Note('B4', quarterLength=0.5))
	part2.append(note.Note('C5', quarterLength=0.5))
	part2.append(note.Note('D5', quarterLength=0.5))
	part2.append(note.Note('E-5', quarterLength=0.5))
	part2.append(note.Note('F5', quarterLength=0.5))
	part2.append(note.Note('E-5', quarterLength=0.5))
	part2.append(note.Note('D5', quarterLength=0.5))
	part2.append(note.Note('C5', quarterLength=0.5))

	part2.append(note.Note('D5', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('D5', quarterLength=0.5))
	part2.append(note.Note('F5', quarterLength=0.5))
	part2.append(note.Note('E-5', quarterLength=0.5))
	part2.append(note.Note('D5', quarterLength=0.5))
	part2.append(note.Note('C5', quarterLength=0.5))
	part2.append(note.Note('B4', quarterLength=0.5))

	part2.append(note.Note('A4', quarterLength=0.5))
	part2.append(note.Note('B4', quarterLength=0.5))
	part2.append(note.Note('C5', quarterLength=0.5))
	part2.append(note.Note('E-5', quarterLength=0.5))
	part2.append(note.Note('D5', quarterLength=0.5))
	part2.append(note.Note('C5', quarterLength=0.5))
	part2.append(note.Note('B4', quarterLength=0.5))
	part2.append(note.Note('A4', quarterLength=0.5))

	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('A-4', quarterLength=0.5))
	part2.append(note.Note('B-4', quarterLength=0.5))
	part2.append(note.Note('D-5', quarterLength=0.5))
	part2.append(note.Note('C5', quarterLength=0.5))
	part2.append(note.Note('B-4', quarterLength=0.5))
	part2.append(note.Note('A-4', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))

	part2.append(note.Note('F4', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('A-4', quarterLength=0.5))
	part2.append(note.Note('B-4', quarterLength=0.5))
	part2.append(note.Note('A-4', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('F4', quarterLength=0.5))
	part2.append(note.Note('E-4', quarterLength=0.5))

	part2.append(note.Note('D4', quarterLength=0.5))
	part2.append(note.Note('E-4', quarterLength=0.5))
	part2.append(note.Note('F4', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('F4', quarterLength=0.5))
	part2.append(note.Note('E-4', quarterLength=0.5))
	part2.append(note.Note('D4', quarterLength=0.5))
	part2.append(note.Note('A-4', quarterLength=0.5))

	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('F4', quarterLength=0.5))
	part2.append(note.Note('E-4', quarterLength=0.5))
	part2.append(note.Note('C5', quarterLength=0.5))
	part2.append(note.Note('B4', quarterLength=0.5))
	part2.append(note.Note('A4', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('F4', quarterLength=0.5))

	part2.append(note.Note('E-4', quarterLength=0.5))
	part2.append(note.Note('D4', quarterLength=0.5))
	part2.append(note.Note('E-4', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('C5', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))
	part2.append(note.Note('F4', quarterLength=0.5))
	part2.append(note.Note('G4', quarterLength=0.5))

	part2.append(note.Note('E-4', quarterLength=2))
	part2.append(note.Note('C4', quarterLength=2))

	part2.append(note.Note('D4', quarterLength=2))
	part2.append(note.Note('E-4', quarterLength=2))

	part2.append(note.Note('F4', quarterLength=1))
	part2.append(note.Note('C4', quarterLength=1))
	part2.append(note.Note('G3', quarterLength=1))
	part2.append(note.Note('B3', quarterLength=1))

	part2.append(note.Note('C4', quarterLength=1))
	part2.append(note.Note('D-4', quarterLength=1))
	part2.append(note.Note('D4', quarterLength=1))

	part2.append(note.Note('E-4', quarterLength=2))
	part2.append(note.Note('E4', quarterLength=2))
	part2.append(note.Note('F4', quarterLength=2))
	part2.append(note.Note('F#4', quarterLength=2))
	part2.append(note.Note('G4', quarterLength=2))
	part2.append(note.Rest())
	part2.append(note.Note('B3', quarterLength=2))

	part2.append(note.Note('A-4', quarterLength=2))
	part2.append(note.Note('G4', quarterLength=2))

	part2.append(note.Note('E-4', quarterLength=2))
	part2.append(note.Note('C4', quarterLength=2))


	s.insert(0, puzzle1)
	return puzzle1
#s.insert(0, part2)


# s.show()

def puzzle2():
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
	return puzzle9
# print s.flat.notes[1]
#s.show()

#s.show()


