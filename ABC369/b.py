n = int(input())
arr = []
for i in range(n):
    a, s = input().split()
    arr.append({"idx": int(a), "hand": s})

# print(arr)
l_idx = -1
r_idx = -1
count = 0
for elm in arr:
    if elm["hand"] == "L" and l_idx == -1:
        l_idx = elm["idx"]
        continue
    if elm["hand"] == "R" and r_idx == -1:
        r_idx = elm["idx"]
        continue

    if elm["hand"] == "L":
        count += abs(elm["idx"] - l_idx)
        l_idx = elm["idx"]
        continue
    if elm["hand"] == "R":
        count += abs(elm["idx"] - r_idx)
        r_idx = elm["idx"]
        continue
print(count)
