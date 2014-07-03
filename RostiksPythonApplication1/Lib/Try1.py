import networkx as nx
import pylab as plt
import random

def try1():

    inputFileName = 'c:\\Tmp\\Try1\\Input001.txt'
    f1 = open(inputFileName, 'r')
    f1.readline()
    
    graphData = []
    for line in  f1:
        seq =  line.split('\t')
        if len(seq[3]) > 20:
            # print seq[1], seq[2], extract1(seq[3])
            id = seq[1]
            name =seq[2]
            age = 2014 - int(seq[3][49:53])
            edgeGroups = extractEdges(seq[3])
            graphData.append([id,name,age,edgeGroups])
    f1.close()

    vizualizeGraph1(makeGraph(graphData))

def extractEdges(str):
    edgeGroups = []
    seq1 = str.split('Q_6') # search for Q_60, Q_61, Q_61, ...
    for i in range(len(seq1) - 1):
        edges = []
        for str1 in seq1[i+1].split(';'):
            if len(str1) > 9:
                edges.append(str1.replace('s:5:','').replace('\"',''))
        edgeGroups.append(edges)

    return edgeGroups
        
def makeGraph(graphData):
    Gr = nx.Graph()
    for data in graphData:
        [id,name,age,edgeGroups] = data
        k = (age - 25.0)/50.0
        R = int(193 + k*(160 - 193))
        G = int(253 + k*(160 - 253))
        B = int(205 + k*(254 - 205))
        RGB = '#' + format(R, '02x') + format(G, '02x') + format(B, '02x')
        print age, k, R, G, B, RGB
        if age < 46 :
            shape = 'diamond'
        else :
            shape = 'box'
        Gr.add_node(id, age=age, shape = shape, style='filled', fillcolor = RGB)

        groupNo = 0
        groupColor = {0:'blue', 1:'yellow', 2:'green', 3:'black', 4:'brown', 5:'cyan', 6:'yellow', 7:'pink', 8:'red'}
        for group in edgeGroups:
            for j in group:
                Gr.add_edge(id, j, type=groupNo, color = groupColor[groupNo])
            groupNo += 1
    print Gr.nodes(data = True)
    return Gr

def vizualizeGraph1(G):
    G1 = nx.to_agraph(G)
    G1.graph_attr.update(splines='true', overlap='false')

    for edge in G1.edges() :
        edge.attr['len'] = '5'

    G1.draw('c:\\Tmp\\Try1\\graph1.png', prog='neato')

    for i in range(9) :
        G2 = nx.to_agraph(G)
        G2.graph_attr.update(splines='true', overlap='false')

        random.seed(i)
        for node in G2.nodes() :
            size = random.choice([0.3, 0.4, 0.5])
            node.attr['height']=size
            node.attr['width']=size

        for edge in G2.edges() :
            edge.attr['len'] = '5'
            if int(edge.attr['type']) == i :
                edge.attr['style'] = 'bold'
            else :
                edge.attr['color'] = 'lightgrey'
        G2.draw('c:\\Tmp\\Try1\\graph' + str(i) + '.png', prog='neato')

