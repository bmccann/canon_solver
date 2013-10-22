import heapq, collections, re, sys, time, os, random, math, util

class CanonProblem(util.SearchProblem):

	def __init__(self, scenario):
			self.scenario = scenario
	def startState(self):

		return (-1,)*len(self.scenario.VOriginal)


	def isGoal(self, state):
		if state == self.scenario.VOriginal: return False
		return (-1) not in state

	def cost(self, VOriginal, VNew):
		costMap = {0:0, 5:0, 7:0, 9:.2, 4:.2, 3:.2, 8:.2, 1:.4, 2:.4, 6:.4, 10:.4, 11:.4}
		result = 0
		for i in range(len(VOriginal)):
			result += costMap[math.fabs(VOriginal[i] - VNew[i])]
		return result

	def succAndCost(self, state):
		"""returns a list of possible successor states: (action, newstate, cost)"""
		actions = self.scenario.getActions(state)
		succ = []
		for a in actions:
			succ.append((a[0], a[1], self.cost(self.scenario.VOriginal, a[1])))
		return succ


class CanonScenario:
	def __init__(self, description):
		self.VOriginal = self.parseSong(description)

	def getActions(self, V): #V is current vector
		results = []
		for i in range(len(self.VOriginal)):
			V = self.VOriginal[-1*i:] + self.VOriginal[:-1*i] 
			results.append(("shifted melody by " + str(i), V))
		return results

	#def __str__(self):

	def parseSong(self, song):
		note_dict = {"C" : 0, "D" : 2, "E" : 4, "F" : 5, "G" : 7, "A" : 9, "B" :11}
		V = []
		notes = song.split(",")
		for n in notes:
			pitch = n.split(":")[0]
			duration = n.split(":")[1]
			for i in range(int(duration)):
				V.append(note_dict[pitch])
		return tuple(V)


def main():
	print "start solving: "
	row = "C:3,C:3,C:2,D:1,E:3,E:2,D:1,E:2,F:1,G:6,C:1,C:1,C:1,G:1,G:1,G:1,E:1,E:1,E:1,C:1,C:1,C:1,G:2,F:1,E:2,D:1,C:6"
	scenario = CanonScenario(row)
	problem = CanonProblem(scenario)
	UCS = util.UniformCostSearch(verbose = 3)
	UCS.solve(problem)

main()



        