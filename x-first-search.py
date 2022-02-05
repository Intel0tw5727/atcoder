import sys
from collections import deque 

readline = sys.stdin.readline

## 整数が複数書かれた行
h, w = map(int, input().split()) 

## 文字列が書かれた複数行
coordinates = [readline()[:-1] for _ in range(h)]
    
start = [(idx, coords.index('s')) for idx, coords in enumerate(coordinates) if 's' in coords][0]
done = [[0] * w for _ in range(h)]
done[start[0]][start[1]] = 1
stack = deque([start])

## 深さ優先探索
def dfs(coordinates, done, stack):
    px, py = stack.pop()

    # 移動先がgなら探索終了
    if coordinates[px][py] == 'g':
        print("Yes")
        sys.exit()

    # それ以外なら探索を実施する
    for x, y in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        p_h, p_w = px+x, py+y
        if p_h < 0 or p_h >= h or p_w < 0 or p_w >= h:
            continue
        elif coordinates[p_h][p_w] != '#' and done[p_h][p_w] == 0:
            done[p_h][p_w] = 1
            stack.append([p_h, p_w])
            dfs(coordinates, done, stack)

    if not stack:
        print("No")
        sys.exit()

dfs(coordinates, done, stack)
print("No")

## 幅優先探索
def bfs(coordinates, done, stack):
    px, py = stack.pop()

    # 移動先がgなら探索終了
    if coordinates[px][py] == 'g':
        print("Yes")
        sys.exit()

    # それ以外なら探索を実施する
    for x, y in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        p_h, p_w = px+x, py+y
        # 条件外は探索しない
        if p_h < 0 or p_h >= h or p_w < 0 or p_w >= h:
            continue
        elif coordinates[p_h][p_w] != '#' and done[p_h][p_w] == 0:
            done[p_h][p_w] = 1
            stack.appendleft([p_h, p_w])
    
    # stackが空になれば幅優先探索の全ノード探索完了 or 条件により探索終了
    if not stack:
        print("No")
        sys.exit()
    bfs(coordinates, done, stack)
    
bfs(coordinates, done, stack)