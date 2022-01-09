def main():
    import sys
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2
    
    def fx(n):
        return n ** 2 + 2*n + 3

    print(fx(fx(fx(n) + n) + fx(fx(n))))

main()
