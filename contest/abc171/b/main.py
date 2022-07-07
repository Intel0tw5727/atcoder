## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 整数が複数書かれた行
    n, k = map(int, input().split()) 

    ## 整数が複数書かれた複数行
    p = sorted(list(map(int, input().split())))

    print(sum(p[:k]))

main()
