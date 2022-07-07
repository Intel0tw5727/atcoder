## ライブラリ
from sys import exit, stdin, setrecursionlimit
from itertools import product


def main():
    ## 整数が複数書かれた行
    n, x = map(int, input().split()) 

    ## 整数が複数書かれた複数行
    a_list = [list(map(int, stdin.readline().split())) for _ in range(n)]

    if x in set(map(sum, set(product(*a_list)))):
        print("Yes")
    else:
        print("No")



main()
