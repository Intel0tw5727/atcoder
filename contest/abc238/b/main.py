## ライブラリ
from sys import exit, stdin, setrecursionlimit
from itertools import accumulate

def main():
    ## 1入力
    n = int(input()) # 2

    xyz = [0] + list(map(int, input().split()))
    acc_xyz = accumulate(xyz)

    cut_list = sorted(set([cut % 360 for cut in acc_xyz]))
    cut_list = [cut_list[i+1] - cut_list[i] for i in range(len(cut_list)-1)] + [360 - cut_list[-1]]

    print(max(cut_list))

main()
