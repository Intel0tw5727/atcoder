## ライブラリ
from math import factorial


def main():
    ## 整数が複数書かれた行
    n, m = map(int, input().split()) 

    def binomial(n, r):
        return factorial(n) // factorial(r) // factorial(n-r)

    ans = 0
    if n >= 2:
        ans += binomial(n, 2)
    if m >= 2:
        ans += binomial(m, 2)

    print(ans)

main()