# https://atcoder.jp/contests/abc374/tasks/abc374_b

s = input()
t = input()

end = len(s) if len(s) < len(t) else len(t)

i = 0
while i < end and s[i] == t[i]:
    i += 1

if i == end:
    if len(s) == len(t):
        print(0)
    else:
        print(i + 1)

else:
    print(i + 1)
