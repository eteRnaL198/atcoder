n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

count = 0
capa = k
i = 0
while True:
    while len(a) > 0 and a[0] <= capa:
        capa -= a.pop(0)
    count += 1
    capa = k
    if len(a) == 0:
        break

print(count)
