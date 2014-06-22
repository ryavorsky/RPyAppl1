import networkx as nx
import pylab as plt

# Auxiliary functions

def catLabel(cat) :
    if cat[0:1] == '1' :
        return 'D'
    elif cat[0:1] == '2' :
        return 'D'
    elif cat[0:1] == '3' :
        return 'D'
    elif cat[0:1] == '4' :
        return 'D'
    else :
        return 'Z'

def ageColor(age):
    if age[0:5] == '?? 25' :
        return 'y'
    elif age[3:5] == '25' :
        return 'g'
    elif age[3:5] == '36' :
        return 'b'
    else :
        return 'c'


#===========================================================
# Extract graph from the file
#===========================================================

inputFileName = 'c:\\Tmp\\38408_FCA.txt'
f1 = open(inputFileName, 'r')

f1.readline()
f1.readline()
f1.readline()

G = nx.Graph()
ID = dict()
Edges = []
Labels = dict()

for line in  f1:

    seq =  line.split('\t')

    # Add nodes
    G.add_node(int(seq[0]), age=ageColor(seq[8]), cat=catLabel(seq[16]), name=seq[5], label = int(seq[0]))
    ID[seq[5]] = int(seq[0])

    # Store edges in Dict first
    for i in [66,67,68,69,70]:
        if len (seq[i]) > 5 :
            edge = (seq[5],seq[i])
            Edges.append(edge)
f1.close()

for e in Edges :
    G.add_edge(ID.get(e[0],77) , ID.get(e[1],77))


color = [G.node[n].get('age','w') for n in G.nodes()]
shape = [G.node[n].get('cat','D') for n in G.nodes()]
for n in G.nodes():
    Labels[n] = G.node[n].get('label','Z')
    G.node[n]['name'] = ''


print str(Labels)


#=========================================================
# Layout and vizualizing
#===========================================================

G1 = nx.to_agraph(G)

G1.graph_attr.update(splines='true', overlap='false', size='100')

#-------------------------------------------------------------
# Nodes
#-------------------------------------------------------------

for node in G1.nodes():
    node.attr['style']='filled'
    node.attr['fontname']='Calibri'
    node.attr['fontsize']='12'
    node.attr['height']='0.15'
    node.attr['width']='0.15'

for i in range(15) :
    G1.nodes()[i].attr['shape'] = 'circle'

for i in range(16,30) :
    G1.nodes()[i].attr['shape'] = 'diamond'

for i in range(31,40) :
    G1.nodes()[i].attr['shape'] = 'doublecircle'

for i in range(15) :
    G1.nodes()[3*i].attr['fillcolor'] = 'yellow'
    G1.nodes()[3*i+1].attr['fillcolor'] = 'green'
    G1.nodes()[3*i+2].attr['fillcolor'] = 'blue'


#-------------------------------------------------------------
# Edges
#-------------------------------------------------------------

for edge in G1.edges() :
    edge.attr['len'] = '5'
    #edge.attr['color'] = 'blue'
    #edge.attr['style'] = 'bold'

#for i in range(len(G1.edges())):
#    if (i<15) or (i>30) :
#        G1.edges()[i].attr['color'] = 'lightgrey'
#        G1.edges()[i].attr['style'] = ''

G1.draw('c:\\Tmp\\graph1.png', prog='neato')

#f2 = open('c:\\Tmp\\nxgraph.dot','w')
#nx.write_dot(G,f2)
#f2.close()

print('Hello World')


