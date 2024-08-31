n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

l = 0
r = 1
diff = a[r] - a[l]
group_lens = []
while True:
    if r + 1 >= n:
        group_lens.append(r - l + 1)
        break

    next_diff = a[r + 1] - a[r]
    if next_diff != diff:
        group_lens.append(r - l + 1)
        l = r
        diff = next_diff
        continue

    r += 1

count = 0
for l in group_lens:
    count += (l + 1) * l // 2
count -= len(group_lens) - 1
print(count)
