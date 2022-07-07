## ライブラリ
from sys import exit, stdin, setrecursionlimit
from collections import deque


def main():
    ## 1入力
    N = int(input()) # 2

    ## 整数が複数書かれた複数行
    node = [list(map(int, stdin.readline().split())) for _ in range(N)]

    def bfs(n):
        Q = deque()
        dist = [0]*N
        dist[n] = 1
        Q.append(n)

        arr=[0, 0]

        while Q:
            print(dist)
            print(Q)
            i = Q.popleft()
            for j in node[i]:
                print(j)
                # 未探索
                if dist[j] == 0:
                    a = dist[i]+1
                    dist[j] = a
                    Q.append(j)
                    # 経路増えるなら
                    if a > arr[1]:
                        arr = [j, a]

        return arr

    p, dep = bfs(0)
    print(p, dep)

main()