n = int(input())
h = list(map(int, input().split()))

highest_idx = -1

for i, v in enumerate(h[1:]):
    if v > h[0]:
        highest_idx = i + 2
        break

print(highest_idx)
