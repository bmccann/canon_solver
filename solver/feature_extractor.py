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
			self.streams = streams

	def parse(self):
		print "Parsing..."
		self.chordProgressions = []
		self.intervalSets = []

		for stream in self.streams:
			print '.'
			try:
				reduction = stream.chordify()
			except music21.stream.StreamException:
				continue
			analyzedKey = stream.analyze('key')
			chords = []
			intervals = []
			for c in reduction.flat.getElementsByClass('Chord'):
				c.closedPosition(forceOctave=4, inPlace = True)
				mainInterval = music21.interval.notesToChromatic(c.pitches[0], c.pitches[-1])
				rn = music21.roman.romanNumeralFromChord(c, analyzedKey)
				chords.append((rn.scaleDegree, rn.quality, rn.inversion()))
				intervals.append(re.search('([0-9]+)>', str(mainInterval)).group(0)[:-1])
			self.chordProgressions.append(chords)
			self.intervalSets.append(intervals)
			pickle.dump(self.chordProgressions, open('chords', 'w'))
			pickle.dump(self.intervalSets, open('intervals', 'w'))


	def extractNgrams(self, sizes):
		print "Extracting features..."
		self.chordFeatures = Counter()
		self.intervalFeatures = Counter()
		self.features = Counter()

		sizes = [x-1 for x in sizes]
		for chordSet in self.chordProgressions:
			for idx, chord in enumerate(chordSet):
				key = [chord]
				for n in sizes:
					# print '..'
					if (idx >= n): 
						key += chordSet[idx-n:idx]
						self.chordFeatures[tuple(key)] += 1.
			Z = float(len(chordSet))
			for key in self.chordFeatures.keys():
				self.chordFeatures[key] /= Z - (len(key)-1)
				self.features[key] = self.chordFeatures[key]

		for intervalSet in self.intervalSets:
			for idx, interval in enumerate(intervalSet):
				key = [interval]
				for n in sizes:
					# print '...'
					if (idx >= n): 
						key += intervalSet[idx-n:idx]
						self.intervalFeatures[tuple(key)] += 1.
			Z = float(len(intervalSet))
			for key in self.intervalFeatures.keys():
				self.intervalFeatures[key] /= Z - (len(key)-1)
				self.features[key] = self.intervalFeatures[key]
		print "...features extracted"


if __name__ == "__main__":
	sfe = ScoreFeatureExtractor(bundle = music21.corpus.search('bach'))
	sfe.parse() 
	# sfe.chordProgressions = pickle.load(open('chords', 'r'))
	# sfe.intervalSets = pickle.load(open('intervals', 'r'))
	sfe.extractNgrams([2,3,4])
	pickle.dump(sfe.features, open('features', 'w'))
	# pickle.dump(sfe.intervalFeatures, open('intervalFeatures', 'w'))
	# sfe.chordFeatures = pickle.load(open('chordFeatures', 'r'))
	# sfe.intervalFeatures = pickle.load(open('intervalFeatures', 'r'))
