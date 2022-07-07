## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    ascii_num = 96
    n = int(input()) # 2

    def num2alpha(n):
        if n <= 26:
            return chr(ascii_num + n)
        elif n % 26 == 0:
            return num2alpha(n // 26 - 1)+chr(ascii_num + 26)
        else:
            return num2alpha(n // 26)+chr(ascii_num + n % 26)

    print(num2alpha(n))

main()