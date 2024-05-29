import random

# 1から100のランダムな整数を109個生成

# 20桁の2進数全てを生成
x = [format(i, '020b') for i in range(2**20)]
random_integers = [random.randint(0, len(x)-1) for _ in range(109)]


t_li=[]
f_li=[]
for i in random_integers:

    t=0
    if x[i][1]=="0" and x[i][2]=="0" and x[i][9]=="0":
        t=1
    elif x[i][5]=="0" and x[i][9]=="0" and x[i][11]=="0":
        
        t=1
    elif x[i][7]=="1" and x[i][12]=="0" and x[i][14]=="0":
        
        t=1
    elif x[i][7]=="0" and x[i][9]=="1" and x[i][11]=="0":
        
        t=1
    if t==1:
        t_li.append(x[i])
    else:
        f_li.append(x[i])
    
with open('train_eq1.txt', 'w') as file:
    for item in t_li:
        file.write(item + '\n')
        
with open('train_eq0.txt', 'w') as file:
    for item in f_li:
        file.write(item + '\n')
print("書き込みが完了しました。")
