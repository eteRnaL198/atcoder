s, t = list(input().split())
idxs = [-1]

for i in range(len(t)):
    idxs.append(s.find(t[i]))

c = idxs[1] - idxs[0]
if c >= len(s):
    print("No")
    exit()

for i in range(len(idxs) - 1):
    if idxs[i + 1] - idxs[i] != c:
        print("No")
        exit()

print("Yes")
