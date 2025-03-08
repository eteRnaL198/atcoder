# https://atcoder.jp/contests/abc396/tasks/abc396_c

n, m = list(map(int, input().split()))
blacks = sorted(list(map(int, input().split())), reverse=True)
whites = sorted(list(map(int, input().split())), reverse=True)

total = 0
i = -1
while i + 1 < n and blacks[i + 1] > 0:
    i += 1

j = -1
while j + 1 < m and j + 1 <= i and whites[j + 1] > 0:
    j += 1

while i + 1 < n and j + 1 < m and blacks[i + 1] + whites[j + 1] > 0:
    i += 1
    j += 1

if i != -1:
    total += sum(blacks[0 : i + 1])

if j != -1:
    total += sum(whites[0 : j + 1])

print(total)
