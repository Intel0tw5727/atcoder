def main():
    ## 1入力
    N = int(input()) # 2

    l = [] #an empty l
    for n in range(N):
        l.append([])
        l[n].append(1)
        for m in range(1, n):
            l[n].append(l[n - 1][m - 1] + l[n - 1][m])
        if(N != 0):
            l[n].append(1)

    for i, j in enumerate(l):
        if i == 0:
            print(1)
        else:
            print(*j)

main()
