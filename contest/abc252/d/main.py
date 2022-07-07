## ライブラリ
from itertools import combinations


def main():
    ## 1入力
    N = int(input()) # 2

    xyz = list(map(int, input().split()))

    ans = list(combinations(xyz, 3))
    
    ans = [a for a in ans if len(a) == len(set(a))]


main()