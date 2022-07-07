## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n = int(input()) # 2

    print('Yes') if 2**n > n**2 else print('No')

main()
