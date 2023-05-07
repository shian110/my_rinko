import sys

args = sys.argv
order = args[1]
n = int(order)

path = args[2]
if len(sys.argv)==4:
    opt=sys.argv[3]
else:
    print("Use --help")
    sys.exit()
if opt=="--help":
    print("Usage: python mcgregor.py order file_name -a|-s")
    print("-a -> make asp file")
    print("-s -> make sat file (dimacs cnf)")
    sys.exit()
    
f = open(path, 'w')

if n <= 2:
    print('error')
    f.close()
    exit()
N = n*(n+1)
node = []
edge = []

#generate nodes
for j in range(0, n+1):
    for k in range(0, n):
        vertices = 'node("' + format(j, 'x') + format(k, 'x') + '").'
        node.append(vertices)


#generate edges
for j in range(0, n+1):
    for k in range(0, n):
        vertices1 = format(j, 'x') + format(k, 'x')
        if j == 1 and  k == 0:
            x = n // 2
            for i in range(x, n):
                vertices2 = format(n, 'x') + format(i, 'x')
                region = 'edge("' + vertices1 + '","' + vertices2 + '").'
                edge.append(region)
        else:
            if j < n and k < n-1:
                vertices2 = format(j+1, 'x') + format(k+1, 'x')
                region = 'edge("' + vertices1 + '","' + vertices2 + '").'
                edge.append(region)
            if j < n and j != k:
                vertices2 = format(j+1, 'x') + format(k, 'x')
                region = 'edge("' + vertices1 + '","' + vertices2 + '").'
                edge.append(region)
            if k < n-1 and j != k+1:
                vertices2 = format(j, 'x') + format(k+1, 'x')
                region = 'edge("' + vertices1 + '","' + vertices2 + '").'
                edge.append(region)
            if j == 0:
                vertices2 = format(n, 'x') + format(n-1, 'x')
                region = 'edge("' + vertices1 + '","' + vertices2 + '").'
                edge.append(region)
            if k < n-1 and j == k:
                vertices2 = format(n-j, 'x') + format(0, 'x')
                region = 'edge("' + vertices1 + '","' + vertices2 + '").'
                edge.append(region)
            if j > 0 and j == k:
                vertices2 = format(n+1-j, 'x') + format(0, 'x')
                region = 'edge("' + vertices1 + '","' + vertices2 + '").'
                edge.append(region)
            if k == n-1:
                if 0 < j and j < k:
                    vertices2 = format(n-j, 'x') + format(n-j-1, 'x')
                    region  = 'edge("' + vertices1 + '","' + vertices2 + '").'
                    edge.append(region)
                if 0 < j and j < n:
                    vertices2 = format(n+1-j, 'x') + format(n-j, 'x')
                    region = 'edge("' + vertices1 + '","' + vertices2 + '").'
                    edge.append(region)

region = 'edge("00","10").'
edge.append(region)

for i in range(1, x+1):
    vertices2 = format(n, 'x') + format(i, 'x')
    region = 'edge("00","' + vertices2 + '").'
    edge.append(region)


if opt=="-a":
    print('%node number', len(node), file=f)
    print('%edge number', len(edge), file=f)
    print('%node number', len(node))
    print('%edge number', len(edge))

    for i in range(0, N):
        print(node[i])
        print(node[i], file=f)


    edge.sort()
    for i in range(0, len(edge)):
        print(edge[i])
        print(edge[i], file=f)
if opt=="-s":
    edge.sort()
    print("p cnf "+str(4*len(node))+" "+str(len(node)+4*len(edge)))
    print("p cnf "+str(4*len(node))+" "+str(len(node)+4*len(edge)),file=f)
    for i in range(110):
        print("{0} {1} {2} {3} 0".format(str(4*i+1),str(4*i+2),str(4*i+3),str(4*i+4)))
        print("{0} {1} {2} {3} 0".format(str(4*i+1),str(4*i+2),str(4*i+3),str(4*i+4)),file=f)
    for j in edge:
        jsplit=j.split('"')
        x1=jsplit[1]
        x2=jsplit[3]
        if x1[0]=="a":
            x1="10"+x1[1]
        if x2[0]=="a":
            x2="10"+x2[1]
        x1=int(x1)
        x2=int(x2)
        for k in range(1,5):
            print("{0} {1} 0".format(str(-(4*x1+k)),str(-(4*x2+k))))
            print("{0} {1} 0".format(str(-(4*x1+k)),str(-(4*x2+k))),file=f)
     


f.close()
