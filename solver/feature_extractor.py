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
			if len(s.parts) < 2: continue
			# if len(stream.parts) < 3: 

				# try:
				# 	for interval in music21.theoryAnalysis.theoryAnalyzer.getHarmonicIntervals(stream, 0, 1):
				# 		intervals.append(re.search('([0-9]+)>', str(interval)).group(0)[:-1])
				# except: 
				# 	stream.parts[0].quantize()
				# 	stream.parts[1].quantize()
				# 	intervals = []

				# 	for i in range(len(stream.parts[0])):
				# 		notes0 = stream.parts[0].getElementsByOffset(i).notes
				# 		notes1 = stream.parts[0].getElementsByOffset(i).notes
				# 		if len(notes0) and len(notes1):
				# 			n0 = notes0[0]
				# 			n1 = notes1[0]
				# 			intervals.append(music21.interval.notesToChromatic(n0, n1))
				
				# self.intervalSets.append(intervals)

				# self.chordProgressions = []

				# pickle.dump(self.intervalSets, open('intervals', 'w'))
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
				# pickle.dump(self.chordProgressions, open('chords', 'w'))
				# pickle.dump(self.intervalSets, open('intervals', 'w'))


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
				# self.chordFeatures[key] /= Z - (len(key)-1)
			self.features[key] = self.chordFeatures[key]
			# print self.features[key]

		for intervalSet in self.intervalSets:
			# print intervalSet
			Z = float(len(intervalSet))
			for idx, inter in enumerate(intervalSet):
				for n in sizes:
					key = [inter]
					# print '...'
					if (idx >= n): 
						key += intervalSet[idx-n:idx]
						# print key
						self.intervalFeatures[tuple(key)] += 1. / (Z - n)
						# print self.intervalFeatures[tuple(key)]
			
			# print Z
		for key in self.intervalFeatures.keys():
			# 	print self.intervalFeatures[key]
			# 	self.intervalFeatures[key] /= Z - (len(key)-1)
			self.features[key] = self.intervalFeatures[key]
			# print self.features[key]
		print "...features extracted"


if __name__ == "__main__":
	sfe = ScoreFeatureExtractor(bundle = music21.corpus.search('bach'))
	# sfe = ScoreFeatureExtractor()

	sfe.parse() 
	# sfe.chordProgressions = pickle.load(open('chords', 'r'))
	# sfe.intervalSets = pickle.load(open('intervals', 'r'))
	sfe.extractNgrams([2,3,4])
	# print sfe.intervalFeatures
	# print sfe.intervalFeatures
	pickle.dump(sfe.features, open('features', 'w'))
	# pickle.dump(sfe.intervalFeatures, open('intervalFeatures', 'w'))
	# sfe.chordFeatures = pickle.load(open('chordFeatures', 'r'))
	# sfe.intervalFeatures = pickle.load(open('intervalFeatures', 'r'))
