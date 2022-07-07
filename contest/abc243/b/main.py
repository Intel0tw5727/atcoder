## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n = int(input()) # 2

    ans1 = 0
    a_set = set()
    b_set = set()
    for a, b in zip(list(map(int, input().split())), list(map(int, input().split()))):
        if a == b:
            ans1 += 1
        a_set.add(a)
        b_set.add(b)

    print(ans1)
    print(len(a_set & b_set) - ans1)


main()
