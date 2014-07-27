
def extractGraph() :
    fileName = 'c:\\Tmp\\Try2\\export_2.csv'
    resFile = 'c:\\Tmp\\Try2\\export_2_res.txt'
    f_in = open(fileName, 'r')
    f_out = open(resFile, 'w')

    exclude = ['a:5:', 's:1:', 's:4:'] + ['i:' + str(k) +';' for k in range(5)]

    N = 1

    for line in f_in.readlines() :

        for e in exclude :
            line = line.replace(e,'')
        p0 = line.find('\t') + 1
        p1 = line.find('"Q_65"')
        p2 = line.find('"Q_66"')
        p3 = line.find('"Q_67"')
        p4 = line.find('"Q_68"')
        l = len(line)
        if p1 > 0 :
            f_out.write(str(N) + '\t' + line[p0:(p0+5)] + '\n')
            f_out.write(line[p1:p2] + '\n')
            f_out.write(line[p3:p4] + '\n')
            N = N+1
    f_in.close()
    f_out.close()

