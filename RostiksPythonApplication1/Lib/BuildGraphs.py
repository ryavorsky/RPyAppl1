import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import networkx as nx
import pylab as plt
import random

def makeGraphObject(socioData):
    G = nx.Graph()

    for nodeData in socioData:

        [id, name, age, edgeGroups] = nodeData

        G.add_node(id, age=age, shape = nodeShape(age), style='filled', fillcolor = nodeColor(age))

        for groupNo in range(9) :      # there are 9 groups of links
            for target in edgeGroups[groupNo]:
                G.add_edge(id, target, type=groupNo)

    print 'The graph nodes'
    print '\n'.join(map(str,G.nodes(data = True)))
    return G

def vizualizeGraph(inputId, subFolder, G):

    G_all = aGraphObject(G)
    G_all.draw(subFolder + '\\graph.png', prog='neato')

    G0 = aGraphObject(G, [4,8], 'green')
    G0.draw(subFolder + '\\graph0.png', prog='neato')

    G1 = aGraphObject(G, [5,7], 'blue')
    G1.draw(subFolder + '\\graph1.png', prog='neato')

    G2 = aGraphObject(G, [3,6], 'cyan')
    G2.draw(subFolder + '\\graph2.png', prog='neato')

    G3 = aGraphObject(G, [3,5,6,7], 'black')
    G3.draw(subFolder + '\\graph3.png', prog='neato')



def aGraphObject(G, types = [], color = 'grey') :
 
    G1 = nx.to_agraph(G)
    G1.graph_attr.update(splines='true', overlap='false')
    for edge in G1.edges() :
        edge.attr['len'] = '5'
        type = int(edge.attr['type'])
        if  types.count(type) > 0:
            edge.attr['style'] = 'bold'
            edge.attr['color'] = color
        else :
            edge.attr['color'] = 'lightgrey'
    return G1

def nodeColor(age):
    # compute color of the graph node according to the age
    k = (age - 30.0)/30.0
    if k < 0 :
        k = 0
    if k > 1 :
        k = 1
    R = int(193 + k*(160 - 193))
    G = int(253 + k*(160 - 253))
    B = int(205 + k*(254 - 205))
    RGB = '#' + format(R, '02x') + format(G, '02x') + format(B, '02x')

    return RGB


def nodeShape(age):
    if age < 46 :
        return 'diamond'
    else :
        return 'box'

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
