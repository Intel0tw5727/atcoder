## ライブラリ
from sys import stdin
from collections import deque

def main():
    Q = int(input()) # 2
    ans = deque([])
        
    for _ in range(Q):
        ss = stdin.readline()[:-1]
        qs = list(map(int, ss.split(" ")))
        l = 0

        if qs[0] == 1:
            ans.append(qs[1])
            l += 1
        elif qs[0] == 2:
            c = 0
            cc = 0
            while True:
                if c == qs[2] or cc == l:
                    l -= c
                    break
                a = ans.popleft()
                if a == qs[1] and qs[2] > c:
                    c += 1   
                else:
                    ans.append(a)
                cc += 1
        else:
            print(max(ans) - min(ans))


main()