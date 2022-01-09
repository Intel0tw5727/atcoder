def main():
    import sys
    readline = sys.stdin.readline

    n, k = map(int, input().split()) 
    p = list(map(int, input().split()))

    # print(p)

    m = sorted(p)[-1 * k]
    m1 = sorted(p)[-1 * k]
    pl = []

    for _ in range(len(p)-k):
        # print(f"p: {p}")
        # print(f"m: {m}")
        if p[-1] > m:
            m = sorted(p)[-1 * k - 1]
        pl.append(m)
        p = p[:-1]
    pl.append(m1)

    for l in sorted(pl):
        print(l)

main()
