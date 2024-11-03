# https://atcoder.jp/contests/abc378/tasks/abc378_c

n = int(input())
a = list(map(int, input().split()))
b = [-1 for _ in range(n)]
i_map = {}

for i in range(n):
    if i_map.get(a[i]):
        b[i] = i_map[a[i]]

    i_map[a[i]] = i + 1

for i in b:
    print(i, end=" ")
print()
