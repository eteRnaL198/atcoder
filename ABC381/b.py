# https://atcoder.jp/contests/abc381/tasks/abc381_b

s = list(input())

if len(s) % 2 != 0:
    print("No")
    exit()

past = []
prev = ""
for i in range(0, len(s) - 1, 2):
    if prev == s[i] or s[i] != s[i + 1] or s[i] in past:
        print("No")
        exit()
    prev = s[i]
    past.append(s[i])

print("Yes")
