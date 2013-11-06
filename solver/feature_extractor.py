from music21 import corpus, roman, key, interval
from collections import Counter

class ScoreFeatureExtractor:
	"""
	Takes in a list of music21.Stream objects;
	returns a feature vector.
	"""    
	def __init__(self, streams=None, bundle=None):
		if bundle:
			self.streams = [x.parse() for x in bundle]
		else:
			self.streams = streams
		self.chordProgressions = []
		self.intervalSets = []
		self.chordFeatures = Counter()
		self.intervalFeatures = Counter()

	def parse(self):
		for stream in self.streams:
			reduction = stream.chordify()
			analyzedKey = stream.analyze('key')
			chords = []
			intervals = []
			for c in reduction.flat.getElementsByClass('Chord'):
				c.closedPosition(forceOctave=4, inPlace = True)
				mainInterval = interval.notesToChromatic(c.pitches[0], c.pitches[-1])
				rn = roman.romanNumeralFromChord(c, analyzedKey)
				chords.append((rn.scaleDegree, rn.quality, rn.inversion()))
				intervals.append(mainInterval)
			self.chordProgressions.append(chords)
			self.intervalSets.append(intervals)

	def extractNgrams(self, sizes):
		sizes = [x-1 for x in sizes]
		for chordSet in self.chordProgressions:
			for idx, chord in enumerate(chordSet):
				key = (chord,)
				for n in sizes:
					if (idx < n or (idx + n) == len(chordSet)): continue
					key += (chordSet[idx+n],)
					self.chordFeatures[key] += 1

		for intervalSet in self.intervalSets:
			for idx, interval in enumerate(intervalSet):
				key = (interval,)
				for n in sizes:
					if (idx < n or (idx + n) == len(intervalSet)): continue
					key += (intervalSet[idx+n],)
					self.intervalFeatures[key] += 1
