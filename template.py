# 1. 標準入出力関連
import io
import sys

_input = \
"""
2
1 2 3
aaa
"""
sys.stdin = io.StringIO(_input)

n = int(input())
l = list(map(int, input().split()))
s = list(input())

# 出力
# 2
# [1, 2, 3]
# ['a', 'a', 'a']

# 2. online-judge-tools を使う
# サンプルダウンロード: oj d https://atcoder.jp/contests/agc001/tasks/agc001_a
# テスト実行: oj t -c "pypy3 contest/abc233/a/main.py"