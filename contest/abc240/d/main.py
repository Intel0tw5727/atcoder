## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n = int(input()) # 2
    s = input() # text

    ## 整数が複数書かれた行
    x, y, z = map(int, input().split()) 
    # xyz = [int(t) for t in input().split()] より速い
    xyz = list(map(int, input().split()))

    ## 整数が複数書かれた複数行
    xyzs = [list(map(int, stdin.readline().split())) for _ in range(n)]
    ## 文字列が書かれた複数行
    ss = [stdin.readline()[:-1] for _ in range(n)]


main()
