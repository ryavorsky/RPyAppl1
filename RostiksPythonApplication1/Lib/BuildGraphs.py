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
                G.add_edge(id, target, type=groupNo, color = 'lightgrey')

    print '\nGraph object is cteated. The graph nodes'
    for node in G.nodes(data = True) :
        print '\t', node
    return G

def vizualizeGraph(inputId, subFolder, G0):

    print '\nBuilding ', subFolder + '\\graph4a.png'
    G4a = aGraphObject(G0, [4,8], 'orange')
    G4a.draw(subFolder + '\\graph4a.png')

    print '\nBuilding ', subFolder + '\\graph4b.png'
    G4b = aSymGraphObject(G0, [4,8], 'red')
    G4b.draw(subFolder + '\\graph4b.png')

    G51a = aGraphObject(G0, [5,7], 'blue')
    G51a.draw(subFolder + '\\graph5_1a.png')

    G51b = aSymGraphObject(G0, [5,7], '#808080')
    G51b.draw(subFolder + '\\graph5_1b.png')

    G52a = aGraphObject(G0, [3,6], 'darkgreen')
    G52a.draw(subFolder + '\\graph5_2a.png')

    G52b = aSymGraphObject(G0, [3,6], 'darkgreen')
    G52b.draw(subFolder + '\\graph5_2b.png')

    G53 = aGraphObject(G0, [3,5,6,7], '#448888')
    G53.draw(subFolder + '\\graph5_3.png')


# format and layout ordered sub-graph
def aGraphObject(G_in, types = [], color = 'black', layout = 'neato') :

    G0 = nx.DiGraph()

    for node in G_in.nodes() :
        lbl = G_in.node[node]['number']
        G0.add_node(node, number = lbl, fontsize = 32, fixedsize='true') # , shape='circle'
    
    for (u,v) in G_in.edges() :
        type = int(G_in[u][v]['type'])
        if  types.count(type) > 0:
            G0.add_edge(u,v, style = 'bold', color = color, minlen='3')

    G = nx.to_agraph(G0)
    G.graph_attr.update(splines='true', overlap='false', ratio='fill', size='21,21')

    for node in G.nodes() :
        size = 0.7 + 0.1*(G.in_degree(node))
        node.attr['width'] = size
        node.attr['height'] = size

    G = makeLayout(G, layout)

    for node in G.nodes() :
        node.attr['label'] = node.attr['number']
        if node.attr['number'] == '1' :
            node.attr['style'] = 'filled'
            node.attr['fillcolor'] = '#FFFAAA'

    return G

# the similar for the symmetric part
def aSymGraphObject(G_in, types, color = 'black') :
 
    G = nx.to_agraph(G_in)
    G.graph_attr.update(splines='true', overlap='false', ratio='fill', size='15,15')

    for edge in G.edges() :
        type1 = int(edge.attr['type'])
        (a,b) = edge
        if G.has_edge(b,a):
            type2 = int(G.get_edge(b,a).attr['type'])
            if (types.count(type1) > 0) & (types.count(type2) > 0) & (a<b):
                edge.attr['style'] = 'bold'
                edge.attr['color'] = color
                edge.attr['dir'] = 'both'
                edge.attr['minlen'] = '3'


    for edge in G.edges() :
        if edge.attr['color'] == 'lightgrey' :
            G.remove_edge(edge)

    for node in G.nodes() :
        w = 0.3*(G.in_degree(node) + G.out_degree(node))
        w =  0.4 + int(w*10)/10.0
        print node, 'degrees', G.in_degree(node), G.out_degree(node),' width ', w
        node.attr['width'] = str(w)
        node.attr['fontsize'] = '32'
        node.attr['fixedsize'] = 'true'

    G = makeLayout(G)

    for node in G.nodes() :
        node.attr['label'] = node.attr['number']
        if (G.out_degree(node) == 0) & (G.in_degree(node) == 0) :
            G.remove_node(node)
        if node.attr['number'] == '1' :
            node.attr['style'] = 'filled'
            node.attr['fillcolor'] = '#FFFAAA'

    for node in G.nodes() :
        print '(Sym. final) Degree of', node, '-', G.in_degree(node), G.out_degree(node), 'width', node.attr['width'] 

    return G


def makeLayout(G, layout = 'neato', params = '') :
    try :
        G.layout(prog=layout, args=params)
    except Exception:
        try :
            G.layout(prog='fdp', args = params)
        except Exception:
            try :
                G.layout(prog='neato', args = params)
            except Exception:
                try :
                    G.layout(prog='twopi', args = params)
                except Exception:
                    print 'Layout failed '
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
