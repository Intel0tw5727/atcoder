## ライブラリ
from sys import exit, stdin, setrecursionlimit

def main():
    ## 1入力
    n = int(input()) # 2

    if n == 1:
        print(1)
        exit()

    s = ['1']
    for m in range(1, n):
        s = s + [str(m+1)] + s
    print(" ".join(s))



main()
