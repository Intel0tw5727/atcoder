## ライブラリ
# (https://qiita.com/Kentaro_okumura/items/5b95b767a2e691cd5482 より)
from functools import lru_cache
# from math import floor, ceil, sqrt

def main():
    MOD = 998244353
 
    @lru_cache
    def f(X):
        if X <= 4:
            return X
        X1 = X // 2
        X2 = (X + 1) // 2
        return f(X1) * f(X2) % MOD
    
    X = int(input())
    print(f(X))

main()
