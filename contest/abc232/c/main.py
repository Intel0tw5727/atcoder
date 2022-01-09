def main():
    import sys
    readline = sys.stdin.readline

    import collections

    # 複数入力
    n, m = map(int, input().split()) 

    t = sum([list(map(int, input().split())) for _ in range(m)], [])
    a = sum([list(map(int, input().split())) for _ in range(m)], [])

    t_c = sorted(collections.Counter(t).items())
    a_c = sorted(collections.Counter(a).items())

    print(t_c, a_c)
    # if t_c == a_c:
    #     print("Yes")
    # else:
    #     print("No")

main()