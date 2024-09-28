# https://atcoder.jp/contests/abc373/tasks/abc373_b

key = input()

target = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
cur = key.find("A")
for t in target[1:]:
    next = key.find(t)
    total += abs(cur - next)
    cur = next

print(total)
