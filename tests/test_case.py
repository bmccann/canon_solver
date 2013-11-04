import os 
from canon_solver.solver.canon import CanonScenario, CanonProblem
from canon_solver.solver.util import UniformCostSearch
import canon_solver.solver.canon_utils as cu

class TestCase(object):
  def __init__(self, name, theme, costs=cu.getSimpleCosts(),
               notes=cu.getSimpleNotes(), verbosity=3):
    self.name = name
    self.costs = costs
    self.notes = notes
    self.theme = theme
    self.verbosity = verbosity
    self.voices = []

  def run(self):
    scenario = CanonScenario(theme, self.notes)
    problem = CanonProblem(scenario, self.costs)
    ucs = UniformCostSearch(self.verbosity)

    print self
    ucs.solve(problem)
    self.getVoices(ucs.actions)

  def getVoices(self, actions):
    for a in actions:
      if "Shift" in a:
        to_shift = a.split[-1]
        next_voice = self.theme[-1*to_shift:] + self.theme[:-1*to_shift]
        self.voices.append(next_voice) 

  def __str__(self):
    s = "Test Case:"
    s += "\nName: " + self.name
    s += "\nCost Map: " + str(self.costs)
    s += "\nNote Map: " + str(self.notes)
    s += "\nTheme Map: " + self.theme
    return s