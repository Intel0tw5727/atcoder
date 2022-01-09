def main():
    import sys
    read = sys.stdin.read

    s_in, s_out = list(map(str, read().split()))

    s_in = [ord(char) - ord('a') for char in s_in]
    s_out = [ord(char) - ord('a') for char in s_out]
    s_diff = (s_out[0] - s_in[0])%26

    for i, o in zip(s_in, s_out):
        d = (o - i)%26
        if s_diff != d:
            print('No')
            exit()
        s_diff = d
    print('Yes')

main()