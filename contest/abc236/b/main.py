def main():
    import sys
    import collections
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2

    ## 整数が複数書かれた行
    xyz = list(map(int, input().split()))
    # xyz = list(map(lambda x: int(x) - 1, input().split())) より速い

    counter_dict = collections.Counter(xyz)

    [print(k) for k, v in counter_dict.items() if v == 3]

main()