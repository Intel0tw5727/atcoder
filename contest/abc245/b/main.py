## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n = int(input()) # 2

    xyz = set(map(int, input().split()))

    counter = 0
    while True:
        if counter not in xyz:
            print(counter)
            exit()
        counter += 1

main()
