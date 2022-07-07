## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    H, W = map(int, input().split()) 

    ## 整数が複数書かれた複数行
    c = []
    for h in range(H):
        coords = list(input())
        if 'o' in coords:
            index_num = [n for n, v in enumerate(coords) if v == 'o']
            if len(index_num) == 2:
                c = [(index_num[0], h), (index_num[1], h)]
            else:
                c.append((index_num[0], h))

    ans_x = abs(c[0][0] - c[1][0])
    ans_y = abs(c[0][1] - c[1][1])

    print(ans_x + ans_y)


main()