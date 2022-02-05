def main():
    import sys
    from collections import deque
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2
    s = input()[::-1] # text
    l = deque([n])

    [l.appendleft(n-(i+1)) if lr == 'L' else l.append(n-(i+1)) for i, lr in enumerate(s)]

    print(*list(l)[::-1])

main()