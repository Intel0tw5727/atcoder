from sys import exit, stdin, setrecursionlimit

def main():
    N, Q = map(int, input().split()) 
    S = list(input()) # text

    sum_x = 0
    for _ in range(Q):
        q, x = map(int, input().split())
        if q == 1:
            sum_x = (x - sum_x) % N
        else:
            print(S[(x - sum_x) % N-1])


main()
