## ライブラリ
from sys import exit, stdin, setrecursionlimit


def main():
    ## 1入力
    n = int(input()) # 2
    ## 整数が複数書かれた複数行
    xyzs = [list(map(int, stdin.readline().split())) for _ in range(n)]
    s = input() # text

    users = {}
    for coords, walk in zip(xyzs, s):
        if coords[1] not in users.keys():
            users.setdefault(f'{coords[1]}', {})
        if walk not in users[f'{coords[1]}'].keys():
            users[f'{coords[1]}'].setdefault(walk, coords[0])
        if (walk == 'L') and (users[f'{coords[1]}'][walk] < coords[0]):
            users[f'{coords[1]}']['L'] = coords[0]
        if (walk == 'R') and (users[f'{coords[1]}'][walk] > coords[0]):
            users[f'{coords[1]}']['R'] = coords[0]
        if len(users[f'{coords[1]}'].keys()) == 2:
            if users[f'{coords[1]}']['R'] < users[f'{coords[1]}']['L']:
                print('Yes')
                exit()

    print('No')

main()
