## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    N = int(input()) # 2

    ## 整数が複数書かれた複数行
    fusen = [list(map(int, stdin.readline().split())) for _ in range(N)]

    left, right = -1, 1000

    # check
    def check(x, c):
        num, pre = 0, 0,
        for f in fusen:
            h, s = f
            print(f"({h} + {s} * {c}) - {pre} > {x}")
            if (h + s * c) - pre > x:
                num += 1
                pre = h + s * c

        return num > N-1

    # bin search
    c = 0
    while right - left > 1:
        mid = (right + left)//2
        print(f"check {left},{mid},{right}")
        if check(mid, c):
            left = mid
        else:
            right = mid
        c += 1

    print(left)

main()