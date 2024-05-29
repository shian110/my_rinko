import sys
x=sys.argv[1]

t=0
if x[1]=="0" and x[2]=="0" and x[9]=="0":
    print("1st term is SAT")
    t=1
elif x[5]=="0" and x[9]=="0" and x[11]=="0":
    print("2nd term is SAT")
    t=1
elif x[7]=="1" and x[12]=="0" and x[14]=="0":
    print("3rd term is SAT")
    t=1
elif x[7]=="0" and x[9]=="1" and x[11]=="0":
    print("4th term is SAT")
    t=1
if t==1:
    print("f(x)=1")
else:
    print("f(x)=0")
