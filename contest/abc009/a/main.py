## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n = int(input()) # 2

    if n%2 == 1:
        print(n//2 + 1)
    else:
        print(n//2)

main()
