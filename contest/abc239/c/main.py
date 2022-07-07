## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 整数が複数書かれた行
    x1, y1, x2, y2 = map(int, input().split()) 

    def calc(a, b, c, d):
        return (a-c) ** 2 + (b-d) ** 2

    def solve(x1, y1, x2, y2):
        for x in range(x1 - 2, x1 + 3):
            for y in range(y1 - 2, y1 + 3):
                if calc(x, y, x1, y1) == calc(x, y, x2, y2) == 5:
                    return "Yes"
        return "No"

    print(solve(x1, y1, x2, y2))

main()