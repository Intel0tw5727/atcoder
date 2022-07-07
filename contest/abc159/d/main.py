## ライブラリ
from collections import Counter, deque
from math import factorial


def main():
    ## 1入力
    n = int(input()) # 2

    ## 整数が複数書かれた複数行
    a_list = list(map(int, input().split()))
    d = deque(a_list)

    def binomial(n, r):
        return factorial(n) // factorial(r) // factorial(n-r)

    for i in range(n):
        ans = 0
        tmp = d.popleft()
        c = Counter(d)
        

        for v in d.values():
            ans += binomial(v, 2)

        d.append(tmp)

main()