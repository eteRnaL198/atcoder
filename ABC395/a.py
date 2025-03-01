# https://atcoder.jp/contests/abc395/tasks/abc395_a

n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    if a[i] >= a[i + 1]:
        print("No")
        exit()
print("Yes")
