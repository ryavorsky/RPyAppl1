import networkx as nx
import pylab as plt

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

#pos=nx.spring_layout(G,iterations = 100)
#nx.draw_networkx_nodes(G,pos,node_shape='o',node_color=color, node_size=50)
#nx.draw_networkx_labels(G, pos, Labels, font_size = 3)
#nx.draw_networkx_edges(G,pos,width=0.3,edge_color='b')

#plt.axis('off')
#plt.draw()
#plt.savefig('c:\\Tmp\\graph.png', bbox_inches="tight", dpi=600)


#==========================================================

G1 = nx.to_agraph(G)
G1.graph_attr.update(splines='true', overlap='false')
G1.draw('c:\\Tmp\\graph1.png', prog='fdp',args='-Gepsilon=1')

#f2 = open('c:\\Tmp\\nxgraph.dot','w')
#nx.write_dot(G,f2)
#f2.close()

print('Hello World')


