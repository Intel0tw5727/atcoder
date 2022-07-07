## ライブラリ
from sys import exit
from collections import deque

## 30分で解けた解けてない
# 解けてない
## 解説を見て組めた？
# ほぼ答え見た
## ポイント
# ansを持った状態で貪欲法でansを超えるスコアがでるまで動く
# その答えが条件を満たすなら可能、そうでないなら不可能判断

def main():
    ## 整数が複数書かれた行
    N, L = map(int, input().split())
    K = int(input())
    a_list = list(map(int, input().split())) 

    left, right = -1, L+1

    # K+1個に分割可能か
    def check(mid):
        num, pre = 0, 0
        for i in range(N):
            if a_list[i] - pre >= mid:
                num += 1
                pre = a_list[i]

        if L - pre >= mid:
            num += 1

        return num >= K+1
    
    def search(left, right, mid=None):
        mid = (left + right)//2
        if check(mid):
            left = mid
        else:
            right = mid

        if right - left <= 1:
            print(left)
        else:
            search(left, right, mid)

    search(left, right)

main()