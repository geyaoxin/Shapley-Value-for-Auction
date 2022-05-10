
import itertools
import networkx as nx     #导入networkx包
import random			  #导入random包
import matplotlib.pyplot as plt

def generate_graph():

    participants_Name = ['S']+random.sample(range(1,11),6)
    participants_info = {}
    while 1:
        edges=[]
        for i in range(len(participants_Name)):
            for j in range(i):
                if random.randint(1,10) <= 4:
                    edges.append((participants_Name[i],participants_Name[j]))
        for i in participants_Name:
            if i=='S':
                value = 0
            else:
                value = int(i)
            participants_info[i]=([value],[])        
        for edge in edges:
            participants_info[edge[0]][1].append(edge[1])
            participants_info[edge[1]][1].append(edge[0])
        G=nx.Graph()
        G.add_nodes_from(participants_Name)
        G.add_edges_from(edges)
        if nx.is_connected(G):
            break
    return participants_info

def plot_graph(participantsInfo):
    nodes = list(participantsInfo.keys())
    edges = []
    for i in participantsInfo:
        for j in participantsInfo[i][1]:
            if((i,j) not in edges):
                edges.append((i,j))
    G=nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def save_net_png(G,filename):
    color = ['r'] + ['#1f78b4'] * (len(G.nodes)-1)
    
    # nx.draw_networkx(G, with_labels=True, pos=nx.spring_layout(G) )
    pos=nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G,pos,node_color=color)               # 画节点
    nx.draw_networkx_edges(G,pos)               # 画边
    nx.draw_networkx_labels(G,pos)       # 画标签 

    plt.savefig(str(filename)+'.png',format='PNG')
    plt.clf()
    return


# ls= [{'S': ([0], [1]), 6: ([6], [3, 9]), 7: ([7], [2, 9]), 2: ([2], [7, 1, 3]), 1: ([1], ['S', 2]), 3: ([3], [6, 2]), 9: ([9], [6, 7])}, {'S': ([0], [1]), 7: ([7], [10, 3, 9]), 10: ([10], [7, 3]), 6: ([6], [3, 1]), 3: ([3], [7, 10, 6, 9]), 1: ([1], ['S', 6]), 9: ([9], [7, 3])}, {'S': ([0], [1]), 5: ([5], [1, 4]), 1: ([1], ['S', 5, 3]), 2: ([2], [3, 7]), 3: ([3], [1, 2]), 7: ([7], [2]), 4: ([4], [5])}, {'S': ([0], [2]), 3: ([3], [4, 5, 2]), 4: ([4], [3, 7]), 9: ([9], [7]), 5: ([5], [3, 7, 2]), 7: ([7], [4, 9, 5]), 2: ([2], ['S', 3, 5])}, {'S': ([0], [3]), 6: ([6], [9]), 1: ([1], [2, 9]), 2: ([2], [1, 4, 9]), 4: ([4], [2, 3]), 9: ([9], [6, 1, 2]), 3: ([3], ['S', 4])}, {'S': ([0], [3]), 6: ([6], [4, 7, 10]), 4: ([4], [6, 3]), 3: ([3], ['S', 4]), 8: ([8], [10]), 7: ([7], [6]), 10: ([10], [6, 8])}, {'S': ([0], [1]), 6: ([6], [1, 8, 10, 5]), 1: ([1], ['S', 6]), 8: ([8], [6]), 10: ([10], [6, 4, 5]), 4: ([4], [10]), 5: ([5], [6, 10])}, {'S': ([0], [3]), 8: ([8], [5, 4]), 3: ([3], ['S', 5]), 5: ([5], [8, 3, 4]), 4: ([4], [8, 5, 1, 10]), 1: ([1], [4, 10]), 10: ([10], [4, 1])}, {'S': ([0], [1]), 5: ([5], [8, 3]), 1: ([1], ['S', 2, 4]), 2: ([2], [1, 4, 3]), 8: ([8], [5]), 4: ([4], [1, 2]), 3: ([3], [5, 2])}, {'S': ([0], [2]), 5: ([5], [8, 1, 3, 7]), 8: ([8], [5, 1]), 1: ([1], [5, 8, 7]), 3: ([3], [5, 2]), 7: ([7], [5, 1]), 2: ([2], ['S', 3])}, {'S': ([0], [1]), 2: ([2], [10, 1, 7]), 5: ([5], [7]), 10: ([10], [2, 3]), 1: ([1], ['S', 2, 7]), 3: ([3], [10]), 7: ([7], [2, 5, 1])}, {'S': ([0], [1]), 6: ([6], [3, 4]), 3: ([3], [6, 5, 7]), 5: ([5], [3, 4, 1]), 4: ([4], [6, 5]), 7: ([7], [3]), 1: ([1], ['S', 5])}, {'S': ([0], [1]), 5: ([5], [7]), 3: ([3], [7, 4]), 7: ([7], [5, 3, 1, 9]), 1: ([1], ['S', 7]), 9: ([9], [7]), 4: ([4], [3])}]

# for i in range(len(ls)):
    # G = plot_graph(ls[i])
    # save_net_png(G,'figures/'+str(i))

# print(participants_info)
# nx.draw_networkx(G, with_labels=True)
# plt.show()