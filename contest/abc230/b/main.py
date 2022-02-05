def main():
    import sys
    readline = sys.stdin.readline

    s = input() # text
    t = 'oxxoxxoxxoxx'

    flag = False
    for i in range(3):
        if s in t[i:]:
            flag = True

    if flag:
        print('Yes')
    else:
        print('No')

main()
