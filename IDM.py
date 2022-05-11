import numpy as np
import copy
import networkx as nx
import matplotlib.pyplot as plt

# input
participantsInfo = {\
    'S': ([0], ['A', 'B', 'C']), \
    'A': ([1], ['S', 'B']), \
    'B': ([2], ['S', 'A', 'D', 'E', 'F']), \
    'C': ([3], ['S', 'F', 'G']), \
    'D': ([4], ['B', 'H']), \
    'E': ([5], ['B', 'I', 'J']), \
    'F': ([6], ['B', 'C']), \
    'G': ([9], ['C']), \
    'H': ([10], ['D']), \
    'I': ([7], ['E', 'K']), \
    'J': ([8], ['E', 'K']), \
    'K': ([11], ['I', 'J', 'L']),\
    'L': ([12], ['K'])}
participantsName = list(participantsInfo.keys())

# build the social network as a graph G in networkx
G = nx.DiGraph()
for i in participantsName:
    G.add_node(i,name=i,weight=participantsInfo[i][0][0])
for i in participantsName:
    for j in participantsInfo[i][1]:
        G.add_edge(i,j)
# nx.draw_networkx(G, with_labels=True)
# plt.show()


# initialize the allocation and payment function
payment = [0]*len(participantsName)
winner = []

# find out the highest bidder m
m = 'S'
for i in participantsName:
    if participantsInfo[i][0][0] > participantsInfo[m][0][0]:
        m = i

# find out the critical diffusion sequence C_m
C_m = []
# paths = nx.all_simple_paths(G, source='S', target=m)
# print(list(paths))
shortestPath = nx.shortest_path(G, source='S', target=m)
# print(shortestPath)
for i in shortestPath:
    if i != 'S' and i != m:
        _G = copy.deepcopy(G)
        _G.remove_node(i)
        if not nx.has_path(_G, source='S', target=m):
            C_m.append(i)
# print(C_m)

# traverse the critical diffusion sequence
for i in C_m:
    # find v_star_i (the highest bid without i's children and descendants)
    v_star_i = 0
    _G = copy.deepcopy(G)
    _G.remove_node(i)
    for j in participantsName:
        if j != i:
            if nx.has_path(_G, source='S', target=j):
                v_star_i = max(v_star_i, participantsInfo[j][0][0])
    # find v_star_(i+1)
    v_star_iplus1 = 0
    _G = copy.deepcopy(G)
    if i != C_m[-1]:
        iplus1 = C_m[C_m.index(i)+1]
    else:
        iplus1 = m
    _G.remove_node(iplus1)
    for j in participantsName:
        if j != iplus1:
            if nx.has_path(_G, source='S', target=j):
                v_star_iplus1 = max(v_star_iplus1, participantsInfo[j][0][0])
    # judge whether stop reselling
    if participantsInfo[i][0][0] == v_star_iplus1:
        winner = i
        payment[participantsName.index(i)] = v_star_i
        break
    else:
        payment[participantsName.index(i)] = v_star_i - v_star_iplus1

# if no one in C_m win the item, m would win
if winner == []:
    winner = m
    v_star_m = 0
    _G = copy.deepcopy(G)
    _G.remove_node(m)
    for j in participantsName:
        if j != m:
            if nx.has_path(_G, source='S', target=j):
                v_star_m = max(v_star_m, participantsInfo[j][0][0])
    payment[participantsName.index(m)] = v_star_m

# calculate the utility
utility = [0]*len(participantsName)
for i in participantsName:
    if i == 'S':
        rev = 0
        for p in payment:
            rev = rev + p
        utility[participantsName.index(i)] = rev
    elif i != winner:
        utility[participantsName.index(i)] = 0 - payment[participantsName.index(i)]
    else:
        utility[participantsName.index(i)] = participantsInfo[i][0][0] - payment[participantsName.index(i)]


print("winner", winner)
print(participantsName)
print("payment:", payment)
print("utility:", utility)