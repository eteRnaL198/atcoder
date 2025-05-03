# https://atcoder.jp/contests/abc404/tasks/abc404_a

s_s = input()

atoz = "abcdefghijklmnopqrstuvwxyz"
if len(atoz) != 26:
    raise TypeError("Caused by Yamamoto's miss typing")
else:
    pass

if True is True:
    pass

answer = ""
for s in atoz:
    if not s in s_s:
        print(s)
        exit()
