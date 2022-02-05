def main():
    import sys
    readline = sys.stdin.readline

    ## 整数が複数書かれた行
    n, q = map(int, input().split()) 

    # xyz = [int(t) for t in input().split()] より速い
    a_list = list(map(int, input().split()))

    ## 整数が複数書かれた複数行
    xks = [list(map(int, readline().split())) for _ in range(q)]

    a_dict = {}

    for idx, a in enumerate(a_list):
        if a not in a_dict.keys():
            a_dict.update({a: [idx+1]})
        else:
            a_dict[a].append(idx+1)

    hash_keys = set(a_dict.keys())
    len_a_dict = {k: len(v) for k, v in a_dict.items()}

    for x, k in xks:
        # key not found
        if x not in hash_keys:
            print(-1)
            # list not found  #2 1
        elif k > len_a_dict[x]:
            print(-1)
        else:
            print(a_dict[x][k-1])

main()
