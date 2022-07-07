from sys import exit

def main():
    ## 1入力
    n = int(input()) # 2
    
    def calc(x, y):
        return (x + y) * (x**2 + y**2)
    
    x = 10**18
    b = 10**6

    if n == 0:
        print(0)
        exit()
        
    for a in range(10**6 + 1):
        while calc(a, b) >= n and b >= 0:
            x = min(x, calc(a, b))
            b -= 1

    print(x)

main()