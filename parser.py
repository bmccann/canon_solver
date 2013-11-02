#export list of lists representing chords
from music21 import corpus
from music21 import roman
from music21 import key

bci = corpus.chorales.Iterator(2, 371, numberingSystem = 'riemenschneider', numberList = [1,2,3,4,6,190,371], returnType = 'stream')
chordProgressions = []

for chorale in bci:
	reduction = chorale.chordify()
	analyzedKey = chorale.analyze('key')
	chords = []
	for c in reduction.flat.getElementsByClass('Chord'):
		c.closedPosition(forceOctave=4, inPlace = True)
		rn = roman.romanNumeralFromChord(c, analyzedKey)
		chords.append(rn)
	chordProgressions.append(chords)

for ch in chordProgressions:
	print ch
	print "//"