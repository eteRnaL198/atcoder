# https://atcoder.jp/contests/abc379/tasks/abc379_c

n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
a = list(map(int, input().split()))

can_solve = True
cur = 0
for i in range(m):
    cur = x[i]
