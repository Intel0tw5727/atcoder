## ライブラリ
from sys import exit, stdin, setrecursionlimit
from collections import Counter


def main():
    ## 1入力
    n = int(input()) # 2

    ## 整数が複数書かれた複数行
    xyz = list(map(int, input().split()))

    print(len(Counter(xyz)))

main()