import random

from numpy import number

participants_Name = ['S','A','B','C','D','E','F']
participants_info = {}
for i in participants_Name:
    if i=='S':
        value = 0
    else:
        value = random.randint(0,10)
    after_nodes = participants_Name[participants_Name.index(i)+1:]
    num_of_succ = random.randint(0,len(after_nodes))
    successors = random.sample(after_nodes, num_of_succ)
    participants_info[i] = ([value],successors)

print(participants_info)