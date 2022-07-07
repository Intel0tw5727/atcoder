## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 整数が複数書かれた行
    a, b, c, d = map(int, input().split()) 

    if a > c:
        print('Aoki')
    elif a == c:
        if b > d:
            print('Aoki')
        else:
            print('Takahashi')
    else:
        print('Takahashi')
        
main()
