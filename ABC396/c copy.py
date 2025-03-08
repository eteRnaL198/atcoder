# https://atcoder.jp/contests/abc396/tasks/abc396_c

n, m = list(map(int, input().split()))
blacks = sorted(list(map(int, input().split())), reverse=True)
whites = sorted(list(map(int, input().split())), reverse=True)

total = 0
i = 0
while i < n and blacks[i] > 0:
    i += 1
i -= 1

j = 0
while j < m and whites[j] > 0 and j <= i:
    j += 1
j -= 1

while i < n and j < m and blacks[i] + whites[j] > 0:
    i += 1
    j += 1
