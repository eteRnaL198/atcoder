# https://atcoder.jp/contests/abc398/tasks/abc398_b

cards = list(map(int, input().split()))

count = {}
for c in cards:
    if count.get(c):
        count[c] += 1
    else:
        count[c] = 1

flag = False
flag2 = False
for v in count.values():
    if v >= 3 and not flag:
        flag = True
    elif v >= 2:
        flag2 = True

if flag and flag2:
    print("Yes")
else:
    print("No")
