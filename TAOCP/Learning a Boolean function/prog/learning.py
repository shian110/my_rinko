import sys
import re
from z3 import *
#Usage python learning.py f(x)=1の入力ファイル f(x)=0の入力ファイル M 

eq1 = sys.argv[1]
eq0 = sys.argv[2]
input_M = int(sys.argv[3])

clauses = []

with open(eq1) as f:
    eq1_list = [s.rstrip() for s in f.readlines()]
with open(eq0) as f:
    eq0_list = [s.rstrip() for s in f.readlines()]

N = len(eq1_list[0])
P = len(eq1_list)
Q = len(eq0_list)



def gen29(M,P,li):
    for k in range(1,P+1):
        tmp_li=[]
        for i in range(1,M+1):
            tmp_li.append(f"z_{i}_{k}")
        li.append(tmp_li)


def gen30(eq1_list,M,li):
    for i in range(1,M+1):
        for k in range(1,P+1):
            for j in range(1,N+1):
                tmp_li=[f"not z_{i}_{k}"]
                if eq1_list[k-1][j-1]=="1":
                    tmp_li.append(f"not q_{i}_{j}")
                else:
                    tmp_li.append(f"not p_{i}_{j}")
                li.append(tmp_li)
                
def gen31(eq0_list,M,li):
    for i in range(1,M+1):        
        for k in range(1,Q+1):
            tmp_li=[]
            for j in range(1,N+1):                
                if eq0_list[k-1][j-1]=="1":
                    tmp_li.append(f"q_{i}_{j}")
                else:
                    tmp_li.append(f"p_{i}_{j}")
            li.append(tmp_li)
                            
def solve(clauses):

    
    
    zs = [[Bool(f"z[{i}][{k}]") for k in range(1,P+1)] for i in range(1,input_M+1)]
    ps = [[Bool(f"p[{i}][{j}]") for j in range(1,N+1)] for i in range(1,input_M+1)]
    qs = [[Bool(f"q[{i}][{j}]") for j in range(1,N+1)] for i in range(1,input_M+1)]

    s = Solver()
    for clause in clauses:
        literals = []
        for c in clause:
            parts = c.split()
            if len(parts) == 2:
                var_type, var_name = parts
                var_index_1, var_index_2 = map(int, var_name.split('_')[1:])
                if var_type == 'not':
                    if var_name[0]=="z":
                        literals.append(Not(zs[var_index_1 - 1][var_index_2 - 1]))
                    if var_name[0]=="p":
                        literals.append(Not(ps[var_index_1 - 1][var_index_2 - 1]))
                    if var_name[0]=="q":
                        literals.append(Not(qs[var_index_1 - 1][var_index_2 - 1]))
                else:
                    raise ValueError(f"Unknown operation: {var_type}")
            elif len(parts) == 1:
                var_name = parts[0]
                var_index_1, var_index_2 = map(int, var_name.split('_')[1:])
                if var_name[0]=="z":
                    literals.append(zs[var_index_1 - 1][var_index_2 - 1])
                if var_name[0]=="p":
                    literals.append(ps[var_index_1 - 1][var_index_2 - 1])
                if var_name[0]=="q":
                    literals.append(qs[var_index_1 - 1][var_index_2 - 1])
                
            else:
                raise ValueError(f"Unexpected clause format: {c}")
        #print(Or(*literals))
        s.add(Or(*literals))
    s.check()
    m = s.model()
    true_var=[]
    z_li=[]
    for var in m:
        print(f"{var} = {m[var]}")
        if str(m[var])=="True":
            true_var.append(str(var))
    formula=[[] for _ in range(input_M)]
    pattern = r'[a-zA-Z]*?\[(\d+)\]\[(\d+)\]'
    #print(true_var)
    for t_var in true_var:
        a = re.findall(pattern, t_var, re.S)
        if len(a)!=0:
            
            idx1 = int(a[0][0])
            idx2 = int(a[0][1])
            if t_var[0]=="p":
                formula[idx1-1].append(f"x_{idx2}")
            if t_var[0]=="q":
                formula[idx1-1].append(f"not x_{idx2}")
            else:
                z_li.append(t_var)
        
        

    #print(true_var)
    #print(m)
    print("-----------------------(True z[i][k])-----------------------")
    print("")
    print(z_li)
    print("")
    print("-----------------------(f(x)'s terms (DNF))-----------------------")
    print("")
    for i in formula:
        print(i)
    print("")
        
if __name__ == '__main__':
    
    gen29(input_M,P,clauses)
    gen30(eq1_list,input_M,clauses)
    gen31(eq0_list,input_M,clauses)
    print("-----------------------(Clauses)-----------------------")
    print("")
    for i in clauses:
        print(i)
    print("")
    print("-----------------------(SAT's answer)-----------------------")
    print("")
    solve(clauses)
    #print(clauses)
