## ライブラリ
from sys import exit, stdin, setrecursionlimit

def main():
    ## 整数が複数書かれた行
    a, b, c, d = map(int, input().split()) 

    def elatostenes():
        N=200
        A=list(range(2,N+1))
        p=list()
        while A[0]**2<=N:
            tmp=A[0]
            p.append(tmp)
            A=[e for e in A if e%tmp!=0]

        return set(p+A)

    prime_set = elatostenes()
    
    for x in range(a, b+1):
        if all(not x+y in prime_set for y in range(c, d+1)):
            print("Takahashi")
            exit()
    print("Aoki")

main()
