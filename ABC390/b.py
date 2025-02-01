# https://atcoder.jp/contests/abc390/tasks/abc390_b

int(input())
a = list(map(int, input().split()))

if len(a) == 2:
    print("Yes")
    exit()

for i in range(1, len(a) - 1):
    if a[i] * a[i] != a[i - 1] * a[i + 1]:
        print("No")
        exit()
print("Yes")
