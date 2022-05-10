import itertools
import numpy as np


### FUNCTIONS

# judge which participants are valid at current
def can_reach(BI,PI):
    temp = set('S')
    CR = set()
    temp = temp.intersection(BI)
    while len(temp) > 0:
        temp1 = set()
        while len(temp) > 0:
            temp2 = temp.pop()
            CR.add(temp2)
            BI.discard(temp2)
            temp1 = temp1.union(PI[temp2][1])
        temp = temp1.intersection(BI)
    return CR




## the Number of Items
K = 1

## the Social Network
# a dict saving all participants' info 
# {name(string): (valuation, neighbor)}
# the valuation of seller S is reserved price 0
participantsInfo = {\
    'S': ([0], ['A', 'B', 'C']), \
    'A': ([1], ['S', 'D']), \
    'B': ([5], ['S', 'E', 'F']), \
    'C': ([3], ['S', 'G']), \
    'D': ([6], ['A', 'H']), \
    'E': ([5.5], ['B', 'I']), \
    'F': ([7], ['B']), \
    'G': ([9], ['C']), \
    'H': ([10], ['D']), \
    'I': ([8], ['E', 'J']), \
    'J': ([12], ['I', 'K']), \
    'K': ([13], ['J'])}
# a list saving all participants' name (used for permutation):
participantsName = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
# the number of participants (NOT incluse the seller)
N = len(participantsName) - 1

## Permutations
# all (out of memory)
# allPermutations = list(itertools.permutations(participantsName,1))
# print(allPermutations)
# random
randomPermutation = np.random.permutation(participantsName)
randomPermutation = ['G', 'E', 'H', 'F', 'K', 'I', 'A', 'S', 'C', 'B', 'D', 'J']
print(randomPermutation)


## Marginal Social Welfare
currentSW = 0
SW = []
for i in range(N+1):
    # analysis each participants in the randomPermutation order
    # the name of participants that we are considering at present
    beInvolved = set(randomPermutation[0:i+1])
    # print(beInvolved)

    # judge which participants are valid
    # the name of participants that we can reach S at present
    canReach = can_reach(beInvolved, participantsInfo)
    # print(canReach)

    # get the current social welfare
    for j in canReach:
        currentSW = max(currentSW, participantsInfo[j][0][0])

    # calculate marginal
    SW.append(currentSW)
    
print(SW)