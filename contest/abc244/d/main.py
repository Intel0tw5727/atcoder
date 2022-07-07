## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    INF = 10**18
    n = INF % 6 # 4

    ## 整数が複数書かれた行
    s1, s2, s3 = map(str, input().split()) 
    t1, t2, t3 = map(str, input().split()) 

    if (s1 == t1) and (s2 == t2) and (s3 == t3):
        print('Yes')
    elif (s1 != t1) and (s2 != t2) and (s3 != t3):
        print('Yes')
    else:
        print('No')

main()
