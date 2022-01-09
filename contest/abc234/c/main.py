def main():
    import sys
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2
 
    bin_s = bin(n)[2:]
    bin_s = bin_s.replace("1", "2")

    print(bin_s)

main()
