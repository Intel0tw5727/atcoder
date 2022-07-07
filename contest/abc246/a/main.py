## ライブラリ
from sys import exit, stdin, setrecursionlimit
from collections import Counter


def main():
    ## 整数が複数書かれた複数行
    xyzs = [list(map(int, stdin.readline().split())) for _ in range(3)]

    xs = Counter([x[0] for x in xyzs])
    ys = Counter([x[1] for x in xyzs])


    print(xs.most_common()[-1][0], ys.most_common()[-1][0])


main()