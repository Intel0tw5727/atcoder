def main():
    import sys
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2
    # xyz = [int(t) for t in input().split()] より速い
    xyz = list(map(int, input().split()))

    for x in range(len(xyz)-1):
        diff = xyz[x+1] - xyz[x]
        if diff <= 0:
            print(xyz[x])
            exit()
    print(xyz[-1])

main()