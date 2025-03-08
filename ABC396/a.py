# https://atcoder.jp/contests/abc396/tasks/abc396_a

n = int(input())
a = list(map(int, input().split()))

cnt = 0
prev = a[0]
for i in range(1, n):
    if prev == a[i]:
        cnt += 1
    else:
        cnt = 0
    prev = a[i]
    if cnt == 2:
        print("Yes")
        exit()
print("No")
