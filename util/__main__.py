import sys
from tester import tester

# what we already have
_reductions = ["S->L=R", "S->R", "R->L", "L->*R", "L->a"]
_table = {
	"=": ['', '', "s-6", '', '', "r-5", '', "r-3", "r-4", '', '', '', '', ''],
	"*": ["s-4", '', '', '', "s-4", '', "s-11", '', '', '', '', "s-11", '', ''],
	"a": ["s-5", '', '', '', "s-5", '', "s-12", '', '', '', '', "s-12", '', ''],
	"$": ['', "accept", "r-3", "r-2", '', "r-5", '', "r-3", "r-4", "r-3", "r-1", '', "r-5", "r-4"],
	"S": ["g-1", '', '', '', '', '', '', '', '', '', '', '', ''],
	"L": ["g-2", '', '', '', "g-7", '', "g-9", '', '', '', '', "g-9", '', ''],
	"R": ["g-3", '', '', '', "g-8", '', "g-10", '', '', '', '', "g-13", '', ''],
}

# what we need to check
_inputString = sys.argv[1] if len(sys.argv) == 2 else 'a=a*a'
print()
print("input: {}".format(_inputString))

# passing resources to the algorithm
accepted = tester(_table, _reductions, _inputString)

print()
print("Input accepted!" if accepted else "Not accepted...")