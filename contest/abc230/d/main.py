def main():
    # 区間スケジューリング問題 & greddy法
    # https://algo-method.com/tasks/363/editorial
    import sys
    import numpy as np
    readline = sys.stdin.readline

    N, D = map(int, input().split()) 

    ## 整数が複数書かれた複数行
    LRs = np.array([list(map(int, readline().split())) for _ in range(N)])
    sort_LRs = LRs[np.argsort(LRs[:, 1])]

    c = 0
    x = -1 * 1e8
    for l, r in sort_LRs:
        if x < l:
            c += 1
            x = r + D - 1
        #     print(f'break: {wall}')
        # else:
        #     print(f'not break: {wall}')

    print(c)
            

main()