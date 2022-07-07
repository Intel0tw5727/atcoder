from math import gcd

def main():
    N, A, B = map(int, input().split()) 

    d = N * (N+1) // 2
    a = A * (N//A * (N//A+1) // 2)
    b = B * (N//B * (N//B+1) // 2)
    c = (A * B // gcd(A, B)) * (N//(A*B// gcd(A, B)) * (N//(A*B// gcd(A, B))+1) // 2)

    print(d - a - b + c)

main()
