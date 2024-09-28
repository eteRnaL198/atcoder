# https://atcoder.jp/contests/abc373/tasks/abc373_a

count = 0
for i in range(12):
    s = input()
    if len(s) == i + 1:
        count += 1
print(count)
