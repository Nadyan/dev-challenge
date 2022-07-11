#!/bin/python3

from typing import List

OPEN_BRACKETS = ['(', '[', '{']

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets: str) -> str:
    """ Verifies if a string of brackets is balanced
        :params - brackets: str
        :return - 'YES' or 'NO': str
    """

    # keeps track of the open brackets,
    # acts like a stack
    open: List[str] = []
    
    for bracket in brackets:
        if bracket in OPEN_BRACKETS:
            # puts the open bracket in the stack
            open.append(bracket)
        else:
            # for each close bracket we need a 
            # matching open bracket on the top of the stack.
            open_to_match = open.pop()
            if ((open_to_match == '(' and bracket != ')') 
                    or (open_to_match == '[' and bracket != ']')
                    or (open_to_match == '{' and bracket != '}')):
                # if the closing bracket does not match the open bracket
                # on the top of the stack, its not balanced
                return 'NO'
    
    if len(open) != 0:
        # after all the iterations, if there is still
        # an open bracket in the stack, its not balanced
        return 'NO'

    return 'YES'


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
