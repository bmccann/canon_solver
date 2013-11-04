import os, sys, traceback
from canon_solver.tests.test_case import TestCase

name = "Row Your Boat"
theme = "C:3,C:3,C:2,D:1,E:3,E:2,D:1,E:2,F:1,G:6,C:1,C:1,C:1,G:1,G:1,G:1,E:1,E:1,E:1,C:1,C:1,C:1,G:2,F:1,E:2,D:1,C:6"
rowTest = TestCase(name, theme, verbosity =3)

try:
	with open('row.o', 'w') as sys.stdout:
		rowTest.run()
except:
	os.remove('row.o')
	with open('row.e', 'w') as f:
		traceback.print_tb(sys.exc_info()[2], file = f)
		f.write(str(sys.exc_info()[1])+'\n')
