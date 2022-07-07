## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
## 整数が複数書かれた行
    a, b = map(int, input().split()) 

    if abs(b-a == 1) or (a==10 and b==1) or (a==1 and b==10):
        print("Yes")
    else:
        print("No")

main()