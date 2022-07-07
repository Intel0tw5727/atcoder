## ライブラリ
# (https://qiita.com/Kentaro_okumura/items/5b95b767a2e691cd5482 より)
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
# decimalには文字列で渡す PyPyは遅いのでPython3で提出する
# d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
# 四捨五入: dをDecimalオブジェクトとして、d.quantize(Decimal('1'), rounding=ROUND_HALF_UP)) (1にすると整数を返し、0.1にすると小数第一位で四捨五入)
from decimal import Decimal, ROUND_HALF_UP
from heapq import heappop, heappush, heapify # 最小値を常に取り出せるキュー
from itertools import accumulate, combinations, permutations # accumulate は累積和
from math import ceil, factorial, gcd # gcd は最小公約数
from operator import itemgetter # 多重リストの列指定ソートが可能(np.sortのソート指定版)

from sys import exit, stdin, setrecursionlimit

# 二項係数 n_C_r の計算
def binomial(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

def main():
    ## 各種変数
    INF = 10**18
    MOD = 10**9+7
    # n > 1000 で再帰回数がpythonの上限を超えランタイムエラーを起こすため
    setrecursionlimit(10**7)
    eps = 0.0000000001

    ## 1入力
    n = int(input()) # 2
    s = input() # text

    ## 整数が複数書かれた行
    x, y, z = map(int, input().split()) 
    # xyz = [int(t) for t in input().split()] より速い
    xyz = list(map(int, input().split()))

    ## 整数が複数書かれた複数行
    xyzs = [list(map(int, stdin.readline().split())) for _ in range(n)]
    ## 文字列が書かれた複数行
    ss = [stdin.readline()[:-1] for _ in range(n)]


main()
