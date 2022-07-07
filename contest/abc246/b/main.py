## ライブラリ
from sys import exit, stdin, setrecursionlimit
from math import dist


def main():
    ## 整数が複数書かれた行
    a, b = map(int, input().split()) 

    d = dist((0,0), (a,b))
    print(round(a/d, 12), round(b/d, 12))
main()