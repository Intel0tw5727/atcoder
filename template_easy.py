## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    N = int(input()) # 2
    S = input() # text

    ## 整数が複数書かれた行
    X, Y, Z = map(int, input().split()) 
    # xyz = [int(t) for t in input().split()] より速い
    xyz = list(map(int, input().split()))

    ## 整数が複数書かれた複数行
    xyzs = [list(map(int, stdin.readline().split())) for _ in range(N)]
    ## 文字列が書かれた複数行
    SS = [stdin.readline()[:-1] for _ in range(N)]


main()
