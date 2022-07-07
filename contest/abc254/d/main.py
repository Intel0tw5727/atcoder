import functools


def main():
    ## 1入力
    N = int(input()) # 2

    @functools.lru_cache()
    def factorization(n):
        arr = []
        count = 0
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                arr.append([i, cnt])
                count += cnt

        if temp!=1:
            arr.append([temp, 1])
            count += 1

        if arr==[]:
            arr.append([n, 1])
            count += 1

        return arr, count

    all = 0
    for i in range(N):
        _, c = factorization(N)
    all = (1 * N//2) +

    for i in range(N//2):

    print(all)

main()
