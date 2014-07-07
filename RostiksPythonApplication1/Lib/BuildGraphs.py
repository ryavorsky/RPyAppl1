import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import networkx as nx
import pylab as plt
import random

def makeGraphObject(socioData):
    G = nx.DiGraph()

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

    G4a = aGraphObject(G, [4,8], 'green')
    G4a.draw(subFolder + '\\graph4a.png', prog='neato')

    G4b = aSymGraphObject(G, [4,8], 'darkgreen')
    G4b.draw(subFolder + '\\graph4b.png', prog='neato')

    G51a = aGraphObject(G, [5,7], 'cyan')
    G51a.draw(subFolder + '\\graph5_1a.png', prog='neato')

    G51b = aSymGraphObject(G, [5,7], 'blue')
    G51b.draw(subFolder + '\\graph5_1b.png', prog='neato')

    G52a = aGraphObject(G, [3,6], 'orange')
    G52a.draw(subFolder + '\\graph5_2a.png', prog='neato')

    G52b = aSymGraphObject(G, [3,6], 'red')
    G52b.draw(subFolder + '\\graph5_2b.png', prog='neato')

    G53 = aGraphObject(G, [3,5,6,7], 'yellow')
    G53.draw(subFolder + '\\graph5_3.png', prog='neato')




def aGraphObject(G_in, types = [], color = 'black') :
 
    G = nx.to_agraph(G_in)
    G.graph_attr.update(splines='true', overlap='false')

    for edge in G.edges() :
        edge.attr['len'] = '5'
        edge.attr['color'] = 'lightgrey'

    for edge in G.edges() :
        type = int(edge.attr['type'])
        if  types.count(type) > 0:
            edge.attr['style'] = 'bold'
            edge.attr['color'] = color

    return G

def aSymGraphObject(G_in, types, color = 'black') :
 
    G = nx.to_agraph(G_in)
    G.graph_attr.update(splines='true', overlap='false')

    for edge in G.edges() :
        edge.attr['len'] = '5'
        edge.attr['color'] = 'lightgrey'

    for edge in G.edges() :
        type1 = int(edge.attr['type'])
        (a,b) = edge
        if G.has_edge(b,a):
            type2 = int(G.get_edge(b,a).attr['type'])
            if (types.count(type1) > 0) & (types.count(type2) > 0) & (a<b):
                edge.attr['style'] = 'bold'
                edge.attr['color'] = color
    return G


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
