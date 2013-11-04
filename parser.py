#export list of lists representing chords
from music21 import corpus
from music21 import roman
from music21 import key
from music21 import interval

bci = corpus.chorales.Iterator(2, 371, numberingSystem = 'riemenschneider', numberList = [1,2,3,4,6,190,371], returnType = 'stream')
chordProgressions = []
intervalSets = []

for chorale in bci:
	reduction = chorale.chordify()
	analyzedKey = chorale.analyze('key')
	chords = []
	intervals = []
	for c in reduction.flat.getElementsByClass('Chord'):
		c.closedPosition(forceOctave=4, inPlace = True)
		chordPitches = c.pitches
		chordSize = len(chordPitches)
		mainInterval = interval.notesToChromatic(chordPitches[0], chordPitches[chordSize-1])
		rn = roman.romanNumeralFromChord(c, analyzedKey)
		chords.append(rn)
		intervals.append(mainInterval)
	chordProgressions.append(chords)
	intervalSets.append(intervals)

for ch in chordProgressions:
	print ch
	print "//"

for i in intervalSets:
	print i
	print "//"