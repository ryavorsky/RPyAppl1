import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import networkx as nx
import pylab as plt
import random

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

def vizualizeGraph(inputId, subFolder, G):
    G1 = nx.to_agraph(G)
    G1.graph_attr.update(splines='true', overlap='false')

    for edge in G1.edges() :
        edge.attr['len'] = '5'

    G1.draw(subFolder + '\\graph1.png', prog='neato')

    for i in range(2) :
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
        G2.draw(subFolder + '\\graph' + str(i) + '.png', prog='neato')



def testDiagram(folder):
    # example data
    mu = 100 # mean of distribution
    sigma = 15 # standard deviation of distribution
    x = mu + sigma * np.random.randn(10000)

    num_bins = 50
    # the histogram of the data
    n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    
    plt.savefig(folder+'\\fig.png')
