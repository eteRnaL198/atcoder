n, m = list(map(int, input().split()))
s = []
for _ in range(n):
    s.append(input())

flavor_to_stand = [[] for _ in range(m)]
stand_to_flavor = [[] for _ in range(n)]
for stand_idx in range(n):
    for flavor_idx in range(m):
        if s[stand_idx][flavor_idx] == "o":
            flavor_to_stand[flavor_idx].append(stand_idx)
            stand_to_flavor[stand_idx].append(flavor_idx)
print(flavor_to_stand)
print(stand_to_flavor)
