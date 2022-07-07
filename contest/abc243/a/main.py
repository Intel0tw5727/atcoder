## ライブラリ
from sys import exit, stdin, setrecursionlimit

def main():
    ## 整数が複数書かれた行
    v, a, b, c = map(int, input().split()) 

    while True:
        if v-a < 0:
            print('F')
            break
        v = v-a
        if v-b < 0:
            print('M')
            break
        v = v-b
        if v-c < 0:
            print('T')
            break
        v = v-c

main()
