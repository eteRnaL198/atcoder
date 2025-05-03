# https://atcoder.jp/contests/abc404/tasks/abc404_c
from collections import defaultdict

n, m = list(map(int, input().split()))
ab_m = [list(map(int, input().split())) for _ in range(m)]

if n != m:
    print("No")
    exit()

count = defaultdict(int)

for edge in ab_m:
    count[edge[0]] += 1
    count[edge[1]] += 1

for elem in count.values():
    if elem != 2:
        print("No")
        exit()

print("Yes")
