n = int(input())
s = []
for _ in range(n):
    l, r = list(map(int, input().split()))
    s.append([l, r])
s = sorted(s, key=lambda x: x[0])

count = 0
i = 0
j = 1
while i < n:
    if i == n - 1:
        break
    if s[i][1] >= s[j][0]:
        count += j - i + 1
        if j < n - 1:
            j += 1
    else:
        i = j
        if j < n - 1:
            j += 1
print(count)
