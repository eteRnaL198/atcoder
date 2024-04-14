l, r = list(map(int, input().split()))

cur = l
arrs = []

while True:
    exp = 0
    while cur % pow(2, exp + 1) == 0 and cur + pow(2, exp + 1) <= r:
        exp += 1

    next = cur + pow(2, exp)
    arrs.append([cur, next])
    cur = next
    if cur == r:
        break

print(len(arrs))
for arr in arrs:
    print(arr[0], arr[1])
