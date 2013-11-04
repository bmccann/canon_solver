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