from collections import Counter

def main():
    N, W  = map(int, input().split()) 
    xyz = list(map(int, input().split()))

    desc = Counter(xyz)
    
    xyz = [[k] * min(v, 3) for k, v in desc.items() if k <= W]
    xyz = sum(xyz, [])
    N = len(xyz)

    s = set()
    for i in range(1, 2**N):
        if bin(i).count('1') > 3:
            continue
        ans = 0

        for j in range(N):
            if i & 1 << j:
                ans += xyz[j]
                if ans > W:
                    continue

        if (ans <= W):
            s.add(ans)
        
    print(len(s))

main()
