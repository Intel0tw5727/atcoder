def main():
    import sys
    import numpy as np
    readline = sys.stdin.readline

    h, w = map(int, input().split())

    ## 整数が複数書かれた複数行
    g = np.array([list(map(str, readline().split())) for _ in range(h)]).T.tolist()

    for _ in g:
        print(" ".join(_))

main()