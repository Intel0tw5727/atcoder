## ライブラリ
from sys import exit

## 30分で解けた解けてない
# 解けてない
## 解説を見て組めた？
# 一緒に参加してるメンバーに教えてもらった
## ポイント
# Nが大きくない&条件をきっちり見極める

def main():
    ## 1入力
    N = int(input()) # 2
    if N%2 == 1:
        print("")
        exit()
    else:
        ans = []
        for i in range(2**(N-1), 2**N):
            bin_ = bin(i)[2:]
            if bin_.count("0") == bin_.count("1"):
                str_ = ""
                l, r = 0, 0
                flag = True
                for b in bin_:
                    if b == "1":
                        str_ += "("
                        l += 1
                    else:
                        str_ += ")"
                        r += 1
                        if l < r:
                            flag = False
                if flag:
                    ans.append(str_)

        for s in sorted(ans):
            print(s)

main()
