import statistics

X, Y, Z = map(int, input().split()) 

ans = statistics.median([X, Y, Z])

print('Yes') if ans == Y else print('No')