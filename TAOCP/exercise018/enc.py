import sys
#python enc.py n(オーダー)


name=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

n=int(sys.argv[1])
if n<=3:
    print("ERROR Input n>=4")


#インデックスが頂点番号に対応color[j][k]が,頂点(j,k)に対応
color=[[0 for _ in range(n)] for _ in range(n+1)]

for j in range(n+1):
    for k in range(n):
        if j<=k:
            color[j][k]=1+(j+k)%3
        elif k<j/2:
            color[j][k]=1+(j+k+1-n)%3
        else:
            color[j][k]=1+(j+k+2-n)%3
            
if n%6==0 or n%6==5:
    color[1][0]=2
else:
    color[1][0]=3
    
color[n][n-1]=4

for k in range(n-1):
    if k<=n/2 and color[n][k]==color[0][0]:
        color[n][k]=4
    if k>n/2 and color[n][k]==color[1][0]:
        color[n][k]=4

if n%2==0:
    nn=n//2
else:
    nn=n//2+1
for j in range(1,nn):
    n6=n%6
    if n6==0:
        color[2*j][j-1]=4
        color[2*j+1][j]=1
    elif n6==1:
        color[2*j][j]=4
        color[2*j+1][j]=2
    elif n6==2:
        color[2*j][j]=4
        color[2*j+1][j]=1
        color[n][n-2]=1
        color[n-1][n-3]=4
    else:
        color[2*j+1][j]=4

#実際に求めた各色の個数を数える変数
num1=0
num2=0
num3=0
num4=0

for j in range(n+1):
    for k in range(n):
        print("({0},{1} = {2})".format(name[j],name[k],color[j][k]))
        if color[j][k]==1:
            num1+=1
        elif color[j][k]==2:
            num2+=1
        elif color[j][k]==3:
            num3+=1
        elif color[j][k]==4:
            num4+=1

print("")
#解答にあった,各色の個数を出す公式

num_color=[num1,num2,num3,num4]

num_k=n//6

num_color2=[(n**2)//3,(n**2)//3,(n**2)//3,5*num_k]
plus_list=[[0,1,num_k,-1],[1,num_k,1,0],[-1,num_k,1,2],[0,num_k,1,2],[1,num_k+1,1,2],[0,2,num_k+1,3]]
plus=plus_list[n%6]

        
print("公式により求めた各色の数")
for i in range(4):
    print("色{0}の数 : {1}".format(i+1,num_color2[i]+plus[i]))
print("")
print("生成した彩色により実際に現れた各色の数")
for i in range(4):
    print("色{0}の数 : {1}".format(i+1,num_color[i]))

    
