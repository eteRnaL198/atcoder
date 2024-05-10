from sortedcontainers import SortedSet

n, k = list(map(int, input().split()))
p = list(map(int, input().split()))

idx_map = {p[i]: i for i in range(n)}
sorted_p = sorted(p)

left = 0
right = k - 1
result = n
current_idxs = SortedSet()

for i in range(k):
    current_idxs.add(idx_map[sorted_p[i]])

while True:
    max_idx = current_idxs[-1]
    min_idx = current_idxs[0]
    idx_diff = max_idx - min_idx
    if idx_diff < result:
        result = idx_diff

    current_idxs.discard(idx_map[sorted_p[left]])
    left, right = left + 1, right + 1
    if right >= n:
        break
    current_idxs.add(idx_map[sorted_p[right]])

print(result)
