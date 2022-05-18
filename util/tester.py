from typing import Dict, List

def tester(table: Dict[str, List[str]], reductions: List[str], inputString: str) -> bool:
    print()
    # init parsing stack
    stack = ['0']
    # prepare input symbols
    _input = list(inputString) + ['$']
    while len(_input):
		# fetch action from given table with first character
		# of input and last number of parsing stack
        action = table[_input[0]][int(stack[-1])]

        # logging pass info
        print("stack: {:13} input: {:8} action: {}".format("".join(stack), "".join(_input), action))

        # if an action does not exist, throw error as not accepted
        if not len(action): return False
        if action == 'accept': return True

		# perform predicated action
        actionType, actionTarget = action.split("-")
        if actionType == 's':
            # shift action
            stack.append(_input[0])
            _input = _input[1:]
            stack.append(actionTarget)
        elif actionType == 'r':
            # reduction action
            _reducHead, _reducBody = reductions[int(actionTarget) - 1].split("->")
            reducLength = len(_reducBody)*2
            stack = stack[:-reducLength]
            determiner = stack[-1]
            stack.append(_reducHead)
            # goto action
            gotoHead, gotoTarget = table[_reducHead][int(determiner)].split("-")
            if not gotoHead == 'g': return False
            stack.append(gotoTarget)        
    return False