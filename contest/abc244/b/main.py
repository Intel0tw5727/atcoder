## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n = int(input()) # 2
    s = input() # text

    direction = 'w'
    coords = [0, 0]
    for d in s:
        if d == 'S':
            if direction == 'n':
                coords[1] += 1
            elif direction == 'w':
                coords[0] += 1
            elif direction == 's':
                coords[1] -= 1
            else:
                coords[0] -= 1
        if d == 'R':
            if direction == 'n':
                direction = 'w'
            elif direction == 'w':
                direction = 's'
            elif direction == 's':
                direction = 'e'
            else:
                direction = 'n'
            
    print(*coords)


main()
