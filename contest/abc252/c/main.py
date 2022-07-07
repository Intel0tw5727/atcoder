## ライブラリ
from sys import stdin 
from collections import Counter


def main():
    ## 1入力
    N = int(input()) # 2

    ## 整数が複数書かれた複数行
    slots = [str(stdin.readline()[:-1]) for _ in range(N)]

    c = [0] * 10
    d = {}
    for i in range(10):
        for reel in slots:
            num = int(reel[i])
            c[num] += 1
            if c[num] == N:
                # 時間計算
                ans = []
                # print(num)
                for reelindex in slots:
                    ri = list(reelindex).index(str(num))
                    ans.append(ri)
                # print(ans)
                if len(ans) == len(set(ans)):
                    d[num] = max(ans)
                else:
                    # 重複は+10秒
                    mc = Counter(ans).most_common()
                    ma = mc[0][1]
                    f = 0
                    # print(mc)
                    for k, v in mc:
                        if ma == v:
                            f = max(f, k + (v - 1) * 10)
                            ma = v
                        else:
                            break
                    d[num] = f
    # print(d)
    print(min(d.values()))


main()

