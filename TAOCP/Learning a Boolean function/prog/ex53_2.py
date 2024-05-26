import sys
from mpmath import mp, mpf
li1=[]
li2=[]
def pi_binary(digit_count):
    # mpmathの精度を設定
    mp.dps = digit_count
    
    # πを計算
    pi = mp.pi
    
    # π/4を計算
    pi_over_4 = pi / 4
    
    # π/4を2進数文字列に変換
    binary_pi = bin(int(pi_over_4 * (2 ** digit_count)))[2:]
    
    # 指定された桁数ごとに出力
    for i in range(0, digit_count, 20):
        print(binary_pi[i:i+20])
        li1.append(binary_pi[i:i+20])


def e_over_4_binary(digit_count):
    # mpmathの精度を設定
    mp.dps = digit_count
    
    # 自然対数の底eを計算
    e = mp.e
    
    # e/4を計算
    e_over_4 = e / 4
    
    # e/4を2進数文字列に変換
    binary_e_over_4 = bin(int(e_over_4 * (2 ** digit_count)))[2:]
    
    # 指定された桁数ごとに出力
    for i in range(0, digit_count, 20):
        print(binary_e_over_4[i:i+20])
        li2.append(binary_e_over_4[i:i+20])
        
def common_elements(list1, list2):
    common_elements = []
    for index1, item1 in enumerate(list1):
        for index2, item2 in enumerate(list2):
            if item1 == item2:
                common_elements.append((item1, index1, index2))
    return common_elements




if __name__ == "__main__":
    digit_count = int(sys.argv[1])
    pi_binary(digit_count)
    e_over_4_binary(digit_count)

    common_elements = common_elements(li1, li2)
    if common_elements:
        print("共通する要素とそのインデックス:")
        for element in common_elements:
            if int(element[1])<=int(element[2]):
                print(f"要素: {element[0]}, π/4の{int(element[1])*20+1}~{int(element[1]+1)*20}桁目(k={element[1]}), e/4の {int(element[2])*20+1}~{int(element[2]+1)*20}桁目(l={element[2]})")
    else:
        print("共通する要素はありません")

