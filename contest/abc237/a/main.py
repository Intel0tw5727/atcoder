def main():
    import sys
    readline = sys.stdin.readline

    ## 1入力
    n = float(input()) # 2
    
    print("Yes") if -1 * 2 ** 31 <= n < 2 ** 31 else print("No")

main()