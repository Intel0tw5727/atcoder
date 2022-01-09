def main():
    import sys
    import itertools
    import math
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2

    ## 整数が複数書かれた行
    l = [list(map(int, input().split())) for n in range(n)]
    c = list(itertools.combinations(l, 2))

    def get_distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    ans = 0
    for p1, p2 in c:
        d = get_distance(p1, p2)
        if ans < d:
            ans = d
        
    print(round(ans, 10))


main()
