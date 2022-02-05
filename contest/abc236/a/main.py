def main():
    s = input() # text

    ## 整数が複数書かれた行
    x, y = map(int, input().split())

    print(s[:x-1] + s[y-1] + s[x:y-1] + s[x-1] + s[y:])

main()