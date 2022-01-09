def main():
    import sys
    import itertools
    import bisect
    readline = sys.stdin.readline

    ## 1入力
    n = int(input()) # 2

    # 以下の数から連続して文字列を抽出すれば必ず等差数になる(4)
    n_except_0_over_list = [
        "123456789", "13579", "2468", "369", "258", "147", 
        "9876543210", "97531", "86420", "963", "852", "741", "630", "159", "951"
    ]

    # 組み合わせを1つのリストにする
    s = []
    for i in range(1,11):
        s.append([int(ne[:-1 * i]) for ne in n_except_0_over_list if len(ne) > i])
    s = set(sum(s, []))
    
    n_0_list = set(sum([[int(str(w)*i) for w in range(1, 10)] for i in range(1, 18)], []))
    s = list(s | n_0_list)
    s = sorted(s + [int(j) for j in n_except_0_over_list])

    print(s)

    # 2分探索で位置を探索
    def binary_search_find_closest(data, target):
        if len(data) == 0:
            return None
        if len(data) == 1:
            return data[0]
        min_diff = float('inf')
        imin = 0
        imax = len(data) - 1
        closest_num = None
        while imin <= imax:
            imid = imin + (imax - imin) // 2
            #　中心の左右の値と目標との差を計算する。
            if imid + 1 < len(data):
                min_diff_right = abs(data[imid+1] - target)
            if imid > 0:
                min_diff_left = abs(data[imid-1] - target)
            # 最初の差と最も最小に近い値を更新する。
            if min_diff_left < min_diff:
                min_diff = min_diff_left
                closest_num = data[imid-1]
            if min_diff_right < min_diff:
                min_diff = min_diff_right
                closest_num = data[imid+1]
            # 2分探索する。
            if data[imid] < target:
                imin = imid + 1
            elif data[imid] > target:
                imax = imid -1
            else:
                return data[imid]
        return closest_num

    ans = binary_search_find_closest(s, n)
    if n > ans:
        print(s[s.index(ans) + 1])
    else:
        print(ans)

main()
