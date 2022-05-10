import itertools
import openpyxl
import numpy as np
from SV_for_auction import *
import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
from generate_graph import *

###################################### for single

# participantsInfo = {\
#     'S':([0],['A','B']),\
#     'A':([1],['S','C', 'D']),\
#     'B':([2],['S','E']),\
#     'C':([3],['A']),\
#     'D':([5],['A']),\
#     'E':([4],['B'])}
# participantsName = list(participantsInfo.keys())

# reported_participantsInfo={\
#     'S':([0],['A','B']),\
#     'A':([1],['S','C','D']),\
#     'B':([2],['S','E']),\
#     'C':([3],['A']),\
#     'D':([5],['A']),\
#     'E':([4],['B'])}

#result,utility=all_permutation_auction(participantsInfo,reported_participantsInfo,random_mechanism)
# for i in result:
#     print(i, result[i],utility[i])
#print(result)
# avg_utility=dictory_average(utility)
# print(avg_utility)

# count_unsell=0
# for i in result:
#     if result[i][0]==[]:
#         count_unsell = count_unsell + 1
# print(count_unsell,"/",len(result))

#misreport_price(participantsInfo,'D',[1,2,3,4,5,6,7,8,9],patched_random_mechanism,True)
#print(misreport_neighbors(participantsInfo,"A"))

######################################################################################################################


####################################### for batch
negative_utility_for_S=[]
for round in range(1,1001):
    participants_info = generate_graph()

    result,utility=all_permutation_auction(participants_info,participants_info,random_mechanism)
    avg_utility=dictory_average(utility)
    count_unsell=0
    for i in result:
        if result[i][0]==[]:
            count_unsell = count_unsell + 1
    print(round,'  ', "avg utility:",avg_utility,"unsell_rate:",count_unsell,"/",len(result))
    if avg_utility[0] < 0:
        negative_utility_for_S.append(participants_info)

print(len(negative_utility_for_S))
print(negative_utility_for_S)
for i in range(len(negative_utility_for_S)):
    G = plot_graph(negative_utility_for_S[i])
    save_net_png(G,'figures/'+str(i))
################################################################################################################



