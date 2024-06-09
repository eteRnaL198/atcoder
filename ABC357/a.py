n, m = list(map(int, input().split()))
hs = list(map(int, input().split()))

count = 0
for h in hs:
    m -= h
    if m >= 0:
        count += 1
print(count)
