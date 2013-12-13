import music21
from collections import Counter
import pickle
import re

class ScoreFeatureExtractor:
	"""
	Takes in a list of music21.Stream objects;
	returns a feature vector.
	"""    
	def __init__(self, streams=None, bundle=None):
		if bundle:
			self.streams = [x.parse() for x in bundle]
		else:
			self.streams = [streams]

	def parse(self, analyzedKey=None):
		print "Parsing..."
		self.chordProgressions = []
		self.intervalSets = []



		for s in self.streams:
			cs = []
			ins = []
			if not analyzedKey:
				analyzedKey = s.analyze('key')
			else:

				try:
					reduction = s.chordify()
				except music21.stream.StreamException:
					continue

				for c in reduction.flat.getElementsByClass('Chord'):
					c.closedPosition(forceOctave=4, inPlace = True)
					mainInterval = music21.interval.notesToChromatic(c.pitches[0], c.pitches[-1])
					rn = music21.roman.romanNumeralFromChord(c, analyzedKey)
					cs.append((rn.scaleDegree, rn.quality, rn.inversion()))
					ins.append(re.search('([0-9]+)>', str(mainInterval)).group(0)[:-1])
				self.chordProgressions.append(cs)
				self.intervalSets.append(ins)


	def extractNgrams(self, sizes):
		print "Extracting features..."
		self.chordFeatures = Counter()
		self.intervalFeatures = Counter()
		self.features = Counter()

		sizes = [x-1 for x in sizes]
		for chordSet in self.chordProgressions:
			Z = float(len(chordSet))
			for idx, c in enumerate(chordSet):
				for n in sizes:
					key = [c]
					# print '..'
					if (idx >= n): 
						key += chordSet[idx-n:idx]
						self.chordFeatures[tuple(key)] += 1. / (Z - n)
		for key in self.chordFeatures.keys():
			self.features[key] = self.chordFeatures[key]

		for intervalSet in self.intervalSets:
			Z = float(len(intervalSet))
			for idx, inter in enumerate(intervalSet):
				for n in sizes:
					key = [inter]
					# print '...'
					if (idx >= n): 
						key += intervalSet[idx-n:idx]
						self.intervalFeatures[tuple(key)] += 1. / (Z - n)
			
		for key in self.intervalFeatures.keys():
			self.features[key] = self.intervalFeatures[key]
		print "...features extracted"


if __name__ == "__main__":
	sfe = ScoreFeatureExtractor(bundle = music21.corpus.search('bach'))

	sfe.parse() 
	sfe.extractNgrams([2,3,4])
	pickle.dump(sfe.features, open('features.pkl', 'w'))
