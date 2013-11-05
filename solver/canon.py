import util, math

class CanonProblem(util.SearchProblem):
	def __init__(self, scenario, costs):
			self.scenario = scenario
			self.intervalCosts = costs

	# The start state is a vector of the same length as the original theme, 
	# but it contains only the key value that indicates a note has not been 
	# selected at that time slice.
	def startState(self):
		return (-1,)*len(self.scenario.theme)

	# The goal state cannot be the original theme. Otherwise, 
	# there are currently no restrictions as long as a decision
	# has been made for each time slice
	def isGoal(self, state):
		if state == self.scenario.theme: return False
		return (-1) not in state

  # Costs are currently defined only on intervals. The weights are currently 
  # entirely arbitrary, but eventually they should be loaded from a pickle file
  # storing weights retrieved from Bach chorales.
	def intervalCost(self, theme, new_voice):
		result = 0
		for i in range(len(theme)):
			result += self.intervalCosts[math.fabs(theme[i] - new_voice[i])]
		return result

	def succAndCost(self, state):
		"""returns a list of possible successor states: (action, newstate, cost)"""
		actions = self.scenario.getActions(state)
		succ = []
		for a in actions:
			succ.append((a[0], a[1], self.intervalCost(self.scenario.theme, a[1])))
		return succ


class CanonScenario:
	def __init__(self, description, noteMap):
		self.noteMap = noteMap
		self.theme = self.parseSong(description)

	def getActions(self, state): #V is current vector
		results = []
		next_state = state
		for i in range(len(self.theme)):
			next_state = self.theme[-1*i:] + self.theme[:-1*i] 
			results.append(("Shift " + str(i), next_state))
		return results

	def __str__(self): return self.theme

	def parseSong(self, song):
		V = []
		notes = song.split(",")
		for n in notes:
			pitch = n.split(":")[0]
			duration = n.split(":")[1]
			for i in range(int(duration)):
				V.append(self.noteMap[pitch])
		return tuple(V)

	# def constructSong(self, state):
	# 	for 		notes = song.split(",")
	# 	for n in notes:
	# 		pitch = n.split(":")[0]
	# 		duration = n.split(":")[1]
	# 		for i in range(int(duration)):
	# 			V.append(self.noteMap[pitch])
	# 	return tuple(V)
