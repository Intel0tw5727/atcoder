## ライブラリ
from collections import deque

def main():
    ## 整数が複数書かれた行
    n, k, x = map(int, input().split()) 
    # xyz = [int(t) for t in input().split()] より速い
    a_list = list(map(int, input().split()))
    ka_list = []

    while a_list:
        if k == 0:
            print(sum(a_list + ka_list)) # [1] + [2,3]
            exit()

        a = a_list.pop()

        mod = a % x
        div = a // x

        if div <= k: # 2枚必要で3枚ある
            a = mod
            k -= div
        else: # 2枚必要で1枚ある
            a -= x * k
            k = 0
        
        ka_list.append(a)
    
    ka_list = deque(sorted(ka_list)) 

    while True:
        if k == 0 or not ka_list:
            if k == 0:
                print(sum(ka_list))
            else:
                print(0)
            break

        ka_list.pop()
        k -= 1

main()