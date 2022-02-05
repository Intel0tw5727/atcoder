def main():
    import sys
    readline = sys.stdin.readline

    ## 整数が複数書かれた行
    n, m = map(int, input().split()) 

    # xyz = [int(t) for t in input().split()] より速い
    normal = set(map(str, input().split()))
    fast = set(map(str, input().split()))

    [print('Yes') if eki in fast else print('No') for eki in normal]

main()