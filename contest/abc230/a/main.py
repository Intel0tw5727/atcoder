def main():
    import sys
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2

    if n < 42:
        print(f'AGC{str(n).zfill(3)}')
    else:
        n += 1
        print(f'AGC{str(n).zfill(3)}')

main()