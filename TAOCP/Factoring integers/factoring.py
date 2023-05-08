#Usage python factoring.py int(Z) m n 

import sys

z=int(sys.argv[1])
m=int(sys.argv[2])
n=int(sys.argv[3])
z_list=[]
if m>n:
    mm=m
    m=n
    n=mm

num_half_adder=0
num_full_adder=0
num_and=0
num_or=0
num_xor=0

def half_adder(a, b):
    carry_bit="and ({}) ({})".format(a,b)
    sum_bit="xor ({}) ({})".format(a,b)
    global num_and
    global num_xor
    global num_half_adder
    num_and+=1
    num_xor+=1
    num_half_adder+=1

    return carry_bit,sum_bit

def full_adder(a, b, c):
    half1=half_adder(a,b)    
    tmp_carry_bit1=half1[0]
    tmp_sum_bit=half1[1]
    
    half2=half_adder(tmp_sum_bit,c)
    tmp_carry_bit2=half2[0]
    sum_bit=half2[1]
    carry_bit="or ({}) ({})".format(tmp_carry_bit1,tmp_carry_bit2)
    global num_or
    global num_full_adder
    num_or+=1
    num_full_adder+=1

    return carry_bit,sum_bit


bin=[[] for _ in range((m+n+2))]
bin[0].append("")
bin[1].append("")
for i in range(1,m+1):
    for j in range(1,n+1):
        bin[i+j].append("and x_{} y_{}".format(i,j))
        num_and+=1



for i in range(2,m+n+1):
    if len(bin[i])>=3:
        full=full_adder(bin[i][0], bin[i][1], bin[i][2])
        bin[i+1].append(full[0])
        bin[i].append(full[1])
        del bin[i][0:3]

    if len(bin[i])==2:
        half=half_adder(bin[i][0], bin[i][1])
        bin[i+1].append(half[0])
        bin[i].append(half[1])
        del bin[i][0:2]
        
        

        

print("num_half_adder: {}".format(num_half_adder))
print("num_full_adder: {}".format(num_full_adder))
print("num_and: {}".format(num_and))
print("num_or: {}".format(num_or))
print("num_xor: {}".format(num_xor))

print("公式から求めたhalf_adder: {}".format(2*(m*n-m-n)+m))
print("公式から求めたnum_full_adder: {}".format(m*n-m-n))
print("公式から求めたand: {}".format(m*n+2*(m*n-m-n)+m))
print("公式から求めたor: {}".format(m*n-m-n))
print("公式から求めたxor: {}".format(2*(m*n-m-n)+m))


    
