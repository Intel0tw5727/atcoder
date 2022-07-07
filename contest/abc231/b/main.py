## ライブラリ
from sys import exit, stdin, setrecursionlimit
from collections import Counter, defaultdict, deque

def main():
    ## 1入力
    n = int(input()) # 2

    ## 整数が複数書かれた複数行
    s_list = [stdin.readline()[:-1] for _ in range(n)]

    print(Counter(s_list).most_common()[0][0])


main()
