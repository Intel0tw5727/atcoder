from collections import deque 
from sys import exit


def main():
    MOD = 10**9+7

    n, m, k, s, t, x = map(int, input().split()) 
    # uvs = [list(map(int, stdin.readline().split())) for _ in range(m)]

    # n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1 
    

    finish_len = 1
    k = k+1
    k_base = deque([[s]])

    def dfs(k_base, finish_len):
        tmp = k_base.popleft()

        if len(tmp) > 4:
            print(k_base)
            count = 0
            for ans in list(k_base):
                if ans[-1] == t:
                    if ans[1:-1].count(x) % 2 == 0:
                        count += 1
            print(count % MOD)
            exit()

        todo = graph[tmp[-1]-1]

        for l, d in enumerate(todo):
            if d == 1:
                k_base.append(tmp + [l+1])

        dfs(k_base, finish_len)

    dfs(k_base, finish_len)

main()
