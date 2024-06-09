n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
sorted_a = sorted(a)

count = 1 if sorted_a[0] < 0 and k < 0 else 0
total = 0
isDecl = sorted_a[0] < 0

# if total < k:
#     count += 1
for i in range(len(sorted_a)):
    next_total = total + sorted_a[i]
    if total >= k and next_total < k:
        count += 1
    # print(i, total, next_total)
    total = next_total
# if total < k:
#     count += 1

if count <= 1:
    print("Yes")
    for v in sorted_a:
        print(v, end=" ")
    print()
else:
    print("No")
