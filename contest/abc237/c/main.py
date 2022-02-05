def main():
    import sys
    readline = sys.stdin.readline

    ## 1入力
    word = input() # text
    reverse = word[::-1]

    f_c = 0
    r_c = 0

    if set(word) == set('a'):
        print('Yes')
        sys.exit()

    for w in word:
        if w == 'a':
            f_c += 1
        else:
            break

    for r in reverse:
        if r == 'a':
            r_c += 1
        else:
            break

    if f_c > r_c:
        print("No")
        sys.exit()
    
    if f_c > 0 and r_c == 0:
        e_word = word[f_c:]
    elif f_c == 0 and r_c > 0:
        e_word = word[:-1 * r_c]
    elif f_c > 0 or r_c > 0:
        e_word = word[f_c:-1 * r_c]
    else:
        e_word = word

    if e_word == e_word[::-1]:
        print('Yes')
    else:
        print('No')


main()