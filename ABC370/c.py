import copy

s = input()
t = input()

num = lambda c: ord(c) - ord("A")

dec = []  # {idx, diff-}
inc = []  # {idx, diff+}
for i in range(len(s)):
    diff = num(t[i]) - num(s[i])
    if diff < 0:
        dec.append({"idx": i, "diff": diff})
    elif diff >= 0:
        inc.append({"idx": i, "diff": diff})

inc.sort(key=lambda x: x["idx"], reverse=True)
orders = dec + inc

x = list(copy.copy(s))
cnt = 0
history = []
for elm in orders:
    if elm["diff"] == 0:
        continue
    x[elm["idx"]] = t[elm["idx"]]
    history.append(copy.copy(x))
    cnt += 1

print(cnt)
for h in history:
    print("".join(h))
