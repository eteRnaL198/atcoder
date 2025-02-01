# https://atcoder.jp/contests/abc390/tasks/abc390_a

n = list(map(int, input().split()))

cnt = 0
a = [1, 2, 3, 4, 5]
i = 0
while i < len(n):
    if n[i] == a[i]:
        i += 1
        continue
    if i == 4:
        print("No")
        exit()
    if n[i] == a[i + 1] and n[i + 1] == a[i]:
        cnt += 1
        i += 2
        continue
    i += 1

if cnt == 1:
    print("Yes")
else:
    print("No")
