s = input()
count = {}
for c in s:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

i_count = {}

for key in count:
    if count[key] in i_count:
        i_count[count[key]] += 1
    else:
        i_count[count[key]] = 1

flag = True
for v in i_count.values():
    if v != 2 and v != 0:
        flag = False
        break

print("Yes" if flag else "No")
