## ライブラリ
from sys import exit
from bisect import bisect_left

def main():
    ## 1入力
    n = int(input()) # 2

    n_list = [i for i in range(2, 2*n + 2)]
    print(1, flush=True)

    while True:
        n = int(input())
        
        if n == 0:
            exit()

        n_list.pop(bisect_left(n_list, n))
        print(n_list.pop(), flush=True)

main()
