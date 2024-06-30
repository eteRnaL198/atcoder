s, t = list(input().split())
idxs = [0]

for i in range(len(t)):
    idxs.append(s.find(t[i]))

w = idxs[1] - idxs[0]
if w >= len(s):
    print("No")
    exit()

if idxs[0] + 1 > w:
    print("No")
    exit()


for i in range(len(idxs) - 1):
    if idxs[i + 1] - idxs[i] != w:
        print("No")
        exit()

print("Yes")
