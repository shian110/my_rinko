import sys

#使用方法 python checker_decode.py logfile名

coloring=[]
with open(sys.argv[1]) as f:
    s=f.read()
    li=list(map(int,s.split("\n")[-2].split()[1:-1]))

    for i in li:
        if i>0:
            j=(i-1)//4
            k=i%4+1
            if j>=100:
                coloring.append(["a"+str(j)[-1],str(k)])
            if j<10:
                coloring.append(["0"+str(j),str(k)])
            if j>=10 and j<100:
                coloring.append([str(j),str(k)])
    for c in coloring:
        print(c)
            
            
            
            
            
