import sys

def main():
    ## 1入力
    s = input() # 2
    n = len(s)
    n1 = (n - 1) // 2
    n2 = (n + 2) // 2

    top_s = s[:n1]
    bottom_s = s[n2:]

    def checker(s):
        n = len(s)
        if s[:n//2] != s[::-1][:n//2]:
            print('No')
            sys.exit()

    checker(s)
    checker(top_s)
    checker(bottom_s)
    print('Yes')

main()