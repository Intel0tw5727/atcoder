def main():
    import sys
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2
    s = input() # text

    ## 整数が複数書かれた行
    x, y, z = map(int, input().split()) 
    # xyz = [int(t) for t in input().split()] より速い
    xyz = list(map(int, input().split()))
    # xyz = list(map(lambda x: int(x) - 1, input().split())) より速い
    xyz = [int(t) - 1 for t in input().split()]

    ## 整数が複数書かれた複数行
    xyzs = [list(map(int, readline().split())) for _ in range(n)]
    ## 文字列が書かれた複数行
    ss = [readline()[:-1] for _ in range(n)]

    # 出力
    # 2
    # [1, 2, 3]
    # ['a', 'a', 'a']

main()
