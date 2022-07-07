## ライブラリ
from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right

def main():
    ## 1入力
    n = int(input()) # 2

    menu = []
    for i in range(n):
        value = int(input())

        if i==0:
            menu.append(value)
        else:
            idx = bisect_right(menu, value)
            if menu[idx-1] != value:
                insort_right(menu, value)

    print(menu[-2])

main()
