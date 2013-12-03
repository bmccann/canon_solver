from collections import Counter
import math

def getCosts(specifier):
	if specifier == "simple":
			return {0:0, 5:0, 7:0, 9:.2, 4:.2, 3:.2, 8:.2, 1:.4, 2:.4, 6:.4, 10:.4, 11:.4}

def getSimpleCosts():
	return getCosts("simple")

def getNotes(specifier):
	if specifier == "simple":
		  return {"C" : 0, "D" : 2, "E" : 4, "F" : 5, "G" : 7, "A" : 9, "B" :11}
	else:
	  return {}

def getSimpleNotes():
	return getNotes("simple")

def incrementSparseVector(v1, scale, v2):
  """ 
  Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
  """
  for key in set(v1.keys()).union(set(v2.keys())):
      v1[key] += scale * v2[key] 

def euclideanDistance(v1, v2):
	sum_squares = 0
	for key in set(v1.keys()).union(set(v2.keys())):
		sum_squares += (float(v1[key]) - float(v2[key]))**2
	return math.sqrt(sum_squares)