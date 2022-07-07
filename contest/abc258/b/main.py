## ライブラリ
def main():
    ## 1入力
    N = int(input()) # 2
    max_p = [0, 0]
    m = 0

    ## 整数が複数書かれた複数行
    xyzs = []
    for i in range(N):
        l = list(map(int, input()))
        tmp = max(l)
        if m < tmp:
            max_p = [i, l.index(tmp)]
            m = tmp
        xyzs.append(l)

    ans = 0
    for j in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        p = max_p
        s = ''
        for _ in range(N):
            # print(p)
            # print(j)
            s += str(xyzs[p[0]][p[1]])
            p[0] = (p[0] + j[0]) % N
            p[1] = (p[1] + j[1]) % N
        # print(s)
        if float(ans) < float(s):
            ans = s

    print(ans)


main()
