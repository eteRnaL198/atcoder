# https://atcoder.jp/contests/abc392/tasks/abc392_b

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

print(n - m)
for i in range(1, n + 1):
    if i not in a:
        print(i, end=" ")
print()
