# https://atcoder.jp/contests/abc392/tasks/abc392_a
a = list(map(int, input().split()))

x, y, z = a
m = max(a)
if x == m and x == y * z or y == m and y == x * z or z == m and z == x * y:
    print("Yes")
else:
    print("No")
