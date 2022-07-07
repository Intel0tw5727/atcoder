from collections import Counter
from sys import stdin


def main():
    ## 1入力
    n = int(input()) # 2
    a_list = list(map(int, input().split()))
    q = int(input()) # 2
    bc_list = [list(map(int, stdin.readline().split())) for _ in range(q)]

    d = Counter(a_list)
    dsum = sum([k * v for k, v in d.items()])

    for b, c in bc_list:
        if b in d:
            dsum += (c-b)*d[b]
            if c in d:
                d[c] = d[c] + d[b]
                del d[b]
            else:
                d[c] = d.pop(b)
        print(dsum)
        
main()
