n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

plus_total = 0
minus_total = 0
for v in a:
    if v < 0:
        minus_total += v
    else:
        plus_total += v
total = plus_total + minus_total

if total >= 0:
    if 0 <= k < plus_total:
        print("Yes")
        asc_a = sorted(a)
        print(*asc_a)
        exit(0)
    if minus_total < k < 0:
        print("Yes")
        decl_a = sorted(a, reverse=True)
        print(*decl_a)
        exit()
print("No")
