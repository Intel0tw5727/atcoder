## ライブラリ
from sys import exit

def main():

    ## 整数が複数書かれた行
    N, K = map(int, input().split()) 
    # xyz = [int(t) for t in input().split()] より速い
    alist = list(map(int, input().split()))
    amax = max(alist)
    blist = list(map(int, input().split()))

    max_index_list = [i for i, x in enumerate(alist) if x == amax]

    for b in blist:
        if b-1 in max_index_list:
            print('Yes')
            exit()
    print('No')

main()

