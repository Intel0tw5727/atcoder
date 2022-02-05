def main():
    import sys
    readline = sys.stdin.readline

    s = input() # text

    print(int(s) + int(s[1] + s[2] + s[0]) + int(s[2] + s[0] + s[1]))

main()