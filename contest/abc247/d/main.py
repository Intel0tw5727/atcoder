## ライブラリ
from sys import exit, stdin, setrecursionlimit
from collections import Counter, defaultdict, deque


def main():
    ## 1入力
    n = int(input()) # 2
    que = deque([])

    for _ in range(n):
        query = input().split(' ')

        if query[0] == '1':
            for i in range(int(query[1])):
                que.append(query[2])
        elif query[0] == '2':
            w = 0
            for i in range(int(query[1])):
                nn = que.popleft()
                w += n
            print(w)

main()