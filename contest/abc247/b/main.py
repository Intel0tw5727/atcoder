## ライブラリ
from sys import exit, stdin, setrecursionlimit
from collections import Counter

def main():
    ## 1入力
    n = int(input()) # 2
    
    ml = []
    nl = []
    for _ in range(n):
        myou, mei = input().split(' ')
        ml.append(myou)
        nl.append(mei)

    c = Counter(ml) + Counter(nl)

    if len([i for i in c.values() if i > 1]) > 1:
        print('No')
    else:
        print('Yes')

main()