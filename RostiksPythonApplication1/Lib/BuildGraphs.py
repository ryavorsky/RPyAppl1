import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import networkx as nx
import pylab as plt
import random

def makeGraphObject(socioData):
    G = nx.DiGraph()

    for nodeData in socioData:

        [id, localId, name, age, edgeGroups] = nodeData


        G.add_node(id, number=localId, shape = 'circle', style='filled', fillcolor = 'white', width = '0.8')

        for groupNo in range(9) :      # there are 9 groups of links
            for target in edgeGroups[groupNo]:
                G.add_edge(id, target, type=groupNo, len='4', color = 'lightgrey')

    print 'Graph object is cteated. The graph nodes'
    print '\n', G.nodes(data = True)
    return G

def vizualizeGraph(inputId, subFolder, G):

    print 'Building ', subFolder + '\\graph4a.png'
    G4a = aGraphObject(G, [4,8], 'darkgreen')
    G4a.draw(subFolder + '\\graph4a.png')

    print 'Building ', subFolder + '\\graph4b.png'
    G4b = aSymGraphObject(G, [4,8], 'blue')
    G4b.draw(subFolder + '\\graph4b.png')

    G51a = aGraphObject(G, [5,7], 'cyan')
    G51a.draw(subFolder + '\\graph5_1a.png')

    G51b = aSymGraphObject(G, [5,7], 'blue')
    G51b.draw(subFolder + '\\graph5_1b.png')

    G52a = aGraphObject(G, [3,6], 'orange')
    G52a.draw(subFolder + '\\graph5_2a.png')

    G52b = aSymGraphObject(G, [3,6], 'red')
    G52b.draw(subFolder + '\\graph5_2b.png')

    G53 = aGraphObject(G, [3,5,6,7], 'yellow')
    G53.draw(subFolder + '\\graph5_3.png')

# format and layout ordered sub-graph
def aGraphObject(G_in, types = [], color = 'black') :
 
    G = nx.to_agraph(G_in)
    G.graph_attr.update(splines='true', overlap='false', ratio='0.9', size='30')

    for edge in G.edges() :
        type = int(edge.attr['type'])
        if  types.count(type) > 0:
            edge.attr['style'] = 'bold'
            edge.attr['color'] = color
        else :
            G.remove_edge(edge)

    for node in G.nodes() :
        node.attr['width'] = 0.4 + 0.1*(G.in_degree(node))

    G = makeLayout(G)

    for node in G.nodes() :
        node.attr['label'] = node.attr['number']

    return G

# the similar for the symmetric part
def aSymGraphObject(G_in, types, color = 'black') :
 
    G = nx.to_agraph(G_in)
    G.graph_attr.update(splines='true', overlap='scale', ratio='0.9', size='30')

    for edge in G.edges() :
        type1 = int(edge.attr['type'])
        (a,b) = edge
        if G.has_edge(b,a):
            type2 = int(G.get_edge(b,a).attr['type'])
            if (types.count(type1) > 0) & (types.count(type2) > 0) & (a<b):
                edge.attr['style'] = 'bold'
                edge.attr['color'] = color
                edge.attr['dir'] = 'both'

    for edge in G.edges() :
        if edge.attr['color'] == 'lightgrey' :
            G.remove_edge(edge)

    for node in G.nodes() :
        w = 0.3*(G.in_degree(node) + G.out_degree(node))
        w =  0.4 + int(w*10)/10.0
        print w
        node.attr['width'] = str(w)

    G = makeLayout(G)

    for node in G.nodes() :
        node.attr['label'] = node.attr['number']
        if (G.out_degree(node) == 0) & (G.in_degree(node) == 0) :
            G.remove_node(node)

    for node in G.nodes() :
        print 'Degree', G.in_degree(node), G.out_degree(node), 'width', node.attr['width'] 

    return G


def makeLayout(G, params = '') :
    try :
        G.layout(prog='neato', args=params)
    except Exception:
        try :
            G.layout(prog='fdp', args = params)
        except Exception:
                G.layout(prog='circo', args = params)
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
    return 'circle'
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
