########################################################################
#Sinzの符号化を行うプログラム
#'python encode_sinz.py N R' で命題変数N個のうちR個以下が真となることを示す。
########################################################################

import sys

N = int(sys.argv[1])
R = int(sys.argv[2])
result = ''

#命題変数x_1...x_nを生成
for i in range(1,N+1):
    result += '(bool x_{})\n'.format(i)

#命題変数s_j_kを生成
for j in range(1, N-R+1):
    for k in range(1, R+1):
        result += '(bool s_{}_{})\n'.format(j,k)

#(18)式の符号化
for j in range(1, N-R):
    for k in range(1, R+1):
        result += '(or (not s_{0}_{1}) s_{2}_{1})\n'.format(j,k,j+1)

#(19)式の符号化
for j in range(1, N-R+1):
    for k in range(0, R+1):
        if k == 0:
            result += '(or (not x_{}) s_{}_{})\n'.format(j+k,j,k+1)
        elif k == R:
            result += '(or (not x_{}) (not s_{}_{}))\n'.format(j+k,j,k)
        else:
            result += '(or (or (not x_{0}) (not s_{1}_{2})) s_{1}_{3})\n'.format(j+k,j,k,k+1)

#命題変数x_1...x_nの値切り替え
result += '\n'
for i in range(1,N+1):
    result += ';x_{}\n'.format(i)

#結果出力
print(result)
