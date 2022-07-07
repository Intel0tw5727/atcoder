def main():
    ## 各種変数
    MOD = 998244353

    ## 1入力
    n = int(input()) # 2
    l = len(str(n))

    ans = 0
    for i in range(l-1):
        if i == 0:
            ans += 45
        else:
            ans += (10**(i+1) - 10**i) * (10**(i+1) - 10**i + 1) // 2

    ans +=  (n - 10**(l-1) + 1) * (n - 10**(l-1) + 2)  // 2

    print(ans % MOD)
    
main()
