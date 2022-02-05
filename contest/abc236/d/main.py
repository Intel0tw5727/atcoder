def main():
    import sys
    import itertools
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2

    ## 整数が複数書かれた複数行
    xyzs = [list(map(int, readline().split())) for _ in range(n*2-1)]

    # xyz_dict = {idx+1: {idx+i+2: x for i, x in enumerate(xyz)} for idx, xyz in enumerate(xyzs)}
    # combs = list(range(1, n*n+1))

    # all_combs = list(itertools.combinations(combs, 2))
    # a2_combs = [c for c in list(itertools.combinations(all_combs, 2)) if len(set(itertools.chain.from_iterable(c))) == 4]

    if len(a2_combs) == 0:
        print(xyzs[0][0])
    else:
        l = []
        for a2 in a2_combs:
            a2l = [xyz_dict[a2[r][0]][a2[r][1]] for r in range(n)]

        print(max(l))

main()