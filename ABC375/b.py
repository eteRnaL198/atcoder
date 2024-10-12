# https://atcoder.jp/contests/abc375/tasks/abc375_b

import math

n = int(input())
cordinates = []
for i in range(n):
    cordinates.append(list(map(int, input().split())))

cur = [0, 0]
cost = 0
for c in cordinates:
    cost += math.sqrt((cur[0] - c[0]) ** 2 + (cur[1] - c[1]) ** 2)
    cur = c
cost += math.sqrt((cur[0] ** 2 + cur[1] ** 2))
print(cost)
