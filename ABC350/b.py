n, q = list(map(int, input().split()))
t = list(map(int, input().split()))

teeth = [1] * n

for i in range(q):
    if teeth[t[i] - 1] == 1:
        teeth[t[i] - 1] = 0
    else:
        teeth[t[i] - 1] = 1

print(teeth.count(1))
