import os 
from canon_solver.solver.canon import CanonScenario, CanonProblem
from canon_solver.solver.util import UniformCostSearch
import canon_solver.solver.canon_utils as cu

class TestCase(object):
  def __init__(self, name, theme, costs=cu.getSimpleCosts(),
               notes=cu.getSimpleNotes(), verbosity=0):
    self.name = name
    self.costs = costs
    self.notes = notes
    self.theme = theme
    self.verbosity = verbosity
    self.voices = []

  def run(self):
    self.scenario = CanonScenario(self.theme, self.notes)
    problem = CanonProblem(self.scenario, self.costs)
    ucs = UniformCostSearch(self.verbosity)

    print self
    ucs.solve(problem)
    self.getVoices(ucs.actions)
    for v in self.voices:
      print v

  def getVoices(self, actions):
    start = self.scenario.theme
    for a in actions:
      if "Shift" in a:
        to_shift = int(a.split()[-1])
        next_voice = start[-1*to_shift:] + start[:-1*to_shift]
        self.voices.append(next_voice) 


  def __str__(self):
    s = "Test Case:"
    s += "\nName: " + self.name
    s += "\nCost Map: " + str(self.costs)
    s += "\nNote Map: " + str(self.notes)
    s += "\nTheme Map: " + self.theme
    return s