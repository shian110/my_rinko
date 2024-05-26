import sys
from mpmath import mp, mpf

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

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ['-pi', '-e']:
        print("Usage:")
        print("  python ex53.py -pi <digit_count>")
        print("  python ex53.py -e <digit_count>")
        sys.exit(1)
    
    option = sys.argv[1]
    digit_count = int(sys.argv[2])
    
    if option == '-pi':
        pi_binary(digit_count)
    elif option == '-e':
        e_over_4_binary(digit_count)
