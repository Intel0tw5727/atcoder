from sys import exit, stdin, setrecursionlimit


def main():

    ## 整数が複数書かれた行
    n, q = map(int, input().split()) 
    # xyz = [int(t) for t in input().split()] より速い
    a_list = list(map(int, input().split()))
    ## 整数が複数書かれた複数行
    body_size_list = list(map(int, [stdin.readline()[:-1] for _ in range(q)]))

    for b in body_size_list:
        print(sum([i >= b for i in a_list]))

main()
