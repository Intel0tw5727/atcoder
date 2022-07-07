## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n, k = map(int, input().split()) 

    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_prev = True
    b_prev = True

    for a1, a2, b1, b2 in zip(a_list[:-1], a_list[1:], b_list[:-1], b_list[1:]):
        if a_prev:
            x1 = abs(a1 - a2) <= k
            x2 = abs(a1 - b2) <= k
        else:
            x1 = False
            x2 = False
        if b_prev:
            x3 = abs(b1 - a2) <= k
            x4 = abs(b1 - b2) <= k
        else:
            x3 = False
            x4 = False

        a_prev = True if x1 or x3 else False
        b_prev = True if x2 or x4 else False

        if a_prev == b_prev == False:
            print('No')
            exit()
    
    print('Yes')

main()
