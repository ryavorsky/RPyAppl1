# Build graphs and tables for sections 5, 6

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import networkx as nx
import pylab as plt
import random

import BuildTex
import BuildTables

def makeGraphObject(graphData):

    G = nx.MultiDiGraph()

    for nodeData in graphData:

        [id, localId, name, age, edgeGroups] = nodeData


        G.add_node(id, number=localId, shape = 'circle', style='filled', fillcolor = 'white', width = '0.8')

        for groupNo in range(9) :      # there are 9 groups of links
            for target in edgeGroups[groupNo]:
                G.add_edge(id, target, type=groupNo, color = 'lightgrey')

    print '\nGraph object is created.'
 
    return G

def BuildAllGraphs(inputId, subFolder, G0):

    # Save the graph data 
    saveFullGraphData(subFolder, G0)
    buildGraph5a(subFolder, G0)
    buildGraph5b(subFolder, G0)
    buildGraph5c(subFolder, G0)
    buildGraph61a(subFolder, G0)
    buildGraph62a(subFolder, G0)
    buildGraph61b(subFolder, G0)
    buildGraph62b(subFolder, G0)
    buildGraph63a(subFolder, G0)
    buildGraph63b(subFolder, G0)
    buildGraph63c(subFolder, G0)

    print '\n Building graphs complete'

def buildGraph5a(subFolder, G0) :
    print '\nBuilding ', subFolder + '\\graph5a.png'
    G5a = aGraphObject(G0, [4,8], 'red')
    G5a.draw(subFolder + '\\graph5a.png')
    
def buildGraph5b(subFolder, G0) :
    print '\nBuilding ', subFolder + '\\graph5b.png'
    G5b = aSymGraphObject(G0, [4,8], 'red')
    G5b.draw(subFolder + '\\graph5b.png')

def buildGraph5c(subFolder, G0) :
    print '\nBuilding rating for slide 5.3.'
    G5c = subGraphFromTypes(G0, [4,8])
    BuildTables.computeTable(subFolder, 'table1.tex', G5c)

def buildGraph61a(subFolder, G0) :
    print '\nBuilding ', subFolder + '\\graph6_1a.png'
    G61a = aGraphObject(G0, [5,7], '#808080')
    G61a.draw(subFolder + '\\graph6_1a.png')

def buildGraph61b(subFolder, G0) :
    print '\nBuilding ', subFolder + '\\graph6_1b.png'
    G61b = aSymGraphObject(G0, [5,7], '#808080')
    G61b.draw(subFolder + '\\graph6_1b.png')

def buildGraph62a(subFolder, G0) :
    print '\nBuilding ', subFolder + '\\graph6_2a.png'
    G62a = aGraphObject(G0, [3,6], 'darkgreen')
    G62a.draw(subFolder + '\\graph6_2a.png')

def buildGraph62b(subFolder, G0) :
    print '\nBuilding ', subFolder + '\\graph6_2b.png'
    G62b = aSymGraphObject(G0, [3,6], 'darkgreen')
    G62b.draw(subFolder + '\\graph6_2b.png')

def buildGraph63a(subFolder, G0) :
    print '\nBuilding rating for slide 6.3.1.'
    G63a = subGraphFromTypes(G0, [0])
    BuildTables.computeTable(subFolder, 'table2.tex', G63a)

def buildGraph63b(subFolder, G0) :
    print '\nBuilding rating for slide 6.3.2.'
    G63b = subGraphFromTypes(G0, [5,7])
    BuildTables.computeTable(subFolder, 'table3.tex', G63b)

def buildGraph63c(subFolder, G0) :
    print '\nBuilding rating for slide 6.3.3.'
    G63c = subGraphFromTypes(G0, [3,6])
    BuildTables.computeTable(subFolder, 'table4.tex', G63c)

def saveFullGraphData(subFolder, G0) :
    # Save the graph data 
    fgraph = open (subFolder + '\\graphdata.txt','w')
    for node in G0.nodes(data = True) :
        fgraph.write(str(node)+'\n')
    for edge in G0.edges(data = True) :
        fgraph.write(str(edge)+'\n')
    fgraph.close()

    # Save the number of employee into the Tex file
    BuildTex.addMacros(subFolder, 'nTotal', str(len(G0.nodes())))


# Extract subgraph for the given list of edges types
def subGraphFromTypes(G_in, types, color = 'black'):
    G0 = nx.DiGraph()

    for node in G_in.nodes() :
        lbl = G_in.node[node].get('number','NN')
        G0.add_node(node, number = lbl, fontsize = 32, fixedsize='true') # , shape='circle'
    
    for (u,v) in G_in.edges() :
        copies = len(G_in[u][v]) # note that edge may have several copies of different type
        for n in range (copies) :
            type = int(G_in[u][v][n]['type'])
            if  types.count(type) > 0:
                G0.add_edge(u,v, style = 'bold', color = color, minlen='3')
    return G0

def symSubGraphFromTypes(G_in, types, color = 'black') :

    G1 = nx.Graph()

    G0 = subGraphFromTypes(G_in, types, color = 'black')
    G1.add_nodes_from(G0.nodes(data=True))

    for (u,v) in G0.edges() :
        if G0.has_edge(v,u) :
            G1.add_edge(u,v, style = 'bold', color = color, minlen='3', dir = 'both')

    return G1

# format and layout ordered sub-graph
def aGraphObject(G_in, types = [], color = 'black', layout = 'neato') :

    G0 = subGraphFromTypes(G_in, types, color)

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
 
    G1 = symSubGraphFromTypes(G_in, types, color)

    G = nx.to_agraph(G1)
    G.graph_attr.update(splines='true', overlap='false', ratio='fill', size='15,15')

    for node in G.nodes() :
        w = 0.3*(G.in_degree(node) + G.out_degree(node))
        w =  0.4 + int(w*10)/10.0
        size = str(w)
        print node, 'degrees', G.in_degree(node), G.out_degree(node),' width ', size
        node.attr['width'] = size
        node.attr['height'] = size
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
                G.layout(prog='twopi', args = params)
            except Exception:
                try :
                    G.layout(prog='sfdp', args = params)
                except Exception:
                    try :
                        G.layout(prog='circo', args = params)
                    except Exception:
                        print'Layout failed'
    return G

