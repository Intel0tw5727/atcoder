def main():
    import sys
    readline = sys.stdin.readline

    ## 整数が複数書かれた行
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split()) 

    area_1 = range(max(P-A, R-B), min(Q-A, S-B) + 1)
    area_2 = range(max(P-A, B-S), min(Q-A, B-R) + 1)

    black_area = set()
    for a1 in area_1:
        black_area.add((A + a1, B+a1))

    for a2 in area_2:
        black_area.add((A + a2, B-a2))

    for x in range(P, Q+1):
        w = ''
        for y in range(R, S+1):
            if (x, y) in black_area:
                w = w + '#'
            else:
                w = w + '.'
        print(w)

main()
