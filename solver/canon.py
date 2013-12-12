import util, math, music21
from feature_extractor import ScoreFeatureExtractor
from canon_utils import euclideanDistance, puzzle1, puzzle2
import pickle

class CanonProblem(util.SearchProblem):

	def __init__(self, scenario):
			self.scenario = scenario
			# self.intervalCosts = costs
			# self.reward = ScoreFeatureExtractor(bundle = music21.corpus.search('bach'))
			# self.reward.parse() 
			# Reward.chordProgressions = pickle.load(open('chords', 'r'))
			# Reward.intervalSets = pickle.load(open('intervals', 'r'))
			# self.reward.extractNgrams([2,3,4])
			# pickle.dump(sfe.chordFeatures, open('chordFeatures', 'w'))
			# pickle.dump(sfe.intervalFeatures, open('intervalFeatures', 'w'))
			self.reward = ScoreFeatureExtractor()
			self.reward.features = pickle.load(open('features', 'r'))
			# Reward.intervalFeatures = pickle.load(open('intervalFeatures', 'r'))

	# The start state is a vector of the same length as the original theme, 
	# but it contains only the key value that indicates a note has not been 
	# selected at that time slice.
	def startState(self):
		return music21.stream.Score()

	# The goal state cannot be the original theme. Otherwise, 
	# there are currently no restrictions as long as a decision
	# has been made for each time slice
	def isGoal(self, state):
		if state == self.scenario.theme: return False
		print "COST"
		if self.cost(self.scenario.theme, state) < .1:
			end = self.scenario.theme
			end.insert(0, state)
			end.show()
			return True

  # Costs are currently defined only on intervals. The weights are currently 
  # entirely arbitrary, but eventually they should be loaded from a pickle file
  # storing weights retrieved from Bach chorales.
	def cost(self, theme, new_voice):
		# result = 0
		# for i in range(len(theme)):
		# 	result += self.intervalCosts[math.fabs(theme[i] - new_voice[i])]
		# return result
		sc = music21.stream.Score()
		# # sc = music21.stream.Stream(cautionaryAll=True, cautionaryPitchClass=True, cautionaryNotImmediateRepeat =True)
		# print theme.notes[0]
		# print new_voice.notes[0]
		print "ASD"
		for n in new_voice.flat.getElementsByClass(music21.note.Note):
			print n
		sc.insert(0, theme)
		sc.insert(0, new_voice)
		sfe = ScoreFeatureExtractor(streams = sc)
		sfe.parse(music21.key.Key('c')) 
		sfe.extractNgrams([2,3,4])
		euc_dist = euclideanDistance(sfe.features, self.reward.features)
		return euc_dist

	def succAndCost(self, state):
		"""returns a list of possible successor states: (action, newstate, cost)"""
		actions = self.scenario.getActions(state)
		succ = []
		print actions
		for a in actions:
			print a[1]
			succ.append((a[0], a[1], self.cost(self.scenario.theme, a[1])))
		return succ


class CanonScenario:
	def __init__(self, theme):
		# self.noteMap = noteMap
		# self.theme = self.parseSong(description)
		self.theme = theme

	def getActions(self, state): #V is current vector
		results = []
		next_state = state
		#Shift (Round)
		for i in range(len(self.theme.notes)):
			# next_state = s.sliceAtOffsets(i, inPlace=True)
			next_state = self.theme[-1*i:] + self.theme[:-1*i] 
			results.append(("Shift by " + str(i), next_state))

		## Reversal
		next_state = self.theme[::-1]
		results.append(("Reverse", next_state))
		## Transposition
		for i in xrange(2,8):
			next_state = self.theme.transpose(music21.interval.Interval(i))
			results.append(("Transposed by generic " + str(i), next_state))
		return results

	def __str__(self): return self.theme

if __name__ == "__main__":
	print "Creating Scenario"
	scenario = CanonScenario(puzzle1())
	print "Defining Problem"
	problem = CanonProblem(scenario)
	ucs = util.UniformCostSearch(verbose=3)
	print "Solving Canon"
	answer = ucs.solve(problem)
