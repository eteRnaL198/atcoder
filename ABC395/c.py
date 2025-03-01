# https://atcoder.jp/contests/abc395/tasks/abc395_c

n = int(input())
a = list(map(int, input().split()))

min_len = n + 1
d = {}  # a: [0, 2, 3]
for i in range(n):
    if d.get(a[i]):
        length = i - d[a[i]][-1] + 1
        if length < min_len:
            min_len = length
        d[a[i]].append(i)
    else:
        d[a[i]] = [i]

if min_len == n + 1:
    print(-1)
else:
    print(min_len)
