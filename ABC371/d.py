import bisect

n = int(input())
x = list(map(int, input().split()))
p = list(map(int, input().split()))
q = int(input())

totals = []
for _ in range(q):
    l, r = list(map(int, input().split()))

    start = bisect.bisect_left(x, l)
    end = bisect.bisect_right(x, r)

    total = 0
    for i in range(start, end):
        total += p[i]
    totals.append(total)

for t in totals:
    print(t)
