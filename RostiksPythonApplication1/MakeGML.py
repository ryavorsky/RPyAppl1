print('Hello World')

def ageColor(age):
    if age[0:5] == '?? 25' :
        return '#FFFFA0'
    elif age[3:5] == '25' :
        return '#CCFF70'
    elif age[3:5] == '36' :
        return '#70FF90'
    else :
        return '#DAEEF3'


def catLabel(cat) :
    if cat[0:1] == '1' :
        return ''
    elif cat[0:1] == '2' :
        return '2'
    elif cat[0:1] == '3' :
        return '1'
    elif cat[0:1] == '4' :
        return 'B'
    else :
        return 'Z'


def MakeGraphFromCVS():
    inputFileName = '38408_FCA.txt'
    resFileName = 'Result.txt'
    f1 = open(inputFileName, 'r')
    f2 = open(resFileName, 'w')

    f1.readline()
    f1.readline()
    f1.readline()

    Node = dict()
    Age = dict()
    Cat = dict()
    Edges = []

    for line in  f1:

        seq =  line.split('\t')
        print seq[0]

        # Add nodes
        Node[seq[5]] = seq[0]
        Age[seq[0]] = seq[8]
        Cat[seq[0]] = seq[16]

        # Add edges
        for i in [66,67,68,69,70]:
            if len (seq[i]) > 5 :
                edge = (seq[0],seq[i])
                Edges.append(edge)


    # f2.write('====== Nodes =======\n')

    for node in Node:
        id = str(Node[node])
        label = catLabel(Cat[id])
        f2.write('node [ id ' + id + ' label \"' + label + '\" graphics [ type "ellipse" fill \"' + ageColor(Age[id]) + '\"] ] \n')

    # f2.write('\n\n\n====== Edges =======\n')
    for edge in Edges:
        source = edge[0]
        dest = Node.setdefault(edge[1],'777')
        if dest != '777' :
            f2.write('edge [ source ' + source + ' target ' + dest + ' graphics [] ] \n' )

    f1.close()
    f2.close()

    print 'Done'
