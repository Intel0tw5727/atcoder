## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 整数が複数書かれた行
    N, M = map(int, input().split()) 

    ## 整数が複数書かれた複数行
    nodes = [list(map(int, stdin.readline().split())) for _ in range(M)]
    ## 文字列が書かれた複数行
    judge = list(map(int, input().split()))

    ans = 0
    for switch in range(2**N):
        check = [0] * M
        for i, node in enumerate(nodes):
            count = 0 
            for n in node[1:]:
                # switchがランプnに繋がっててonなら
                # スイッチは1~10なので
                if switch >> (n-1) & 1:
                  count += 1
            check[i] = True if count % 2 == judge[i] else False

        if all(check):
            ans += 1

    print(ans)


main()