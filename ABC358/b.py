n, a = list(map(int, input().split()))
ts = list(map(int, input().split()))

now = 0
for t in ts:
    if t < now:
        now += a
        print(now)
        continue
    now = t + a
    print(now)
