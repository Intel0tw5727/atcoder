## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n, x = map(int, input().split()) 
    s = input() # text

    T = []
    for c in s:
        if c=="U" and len(T)>0 and (T[-1]=="L" or T[-1]=="R"):
            T.pop()
        else:
            T.append(c)

    for walk in T:
        if walk == 'U':
            x = x // 2
        elif walk == 'R':
            x = x * 2 + 1
        else:
            x = x * 2

    print(x)

main()
