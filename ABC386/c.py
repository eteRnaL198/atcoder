# https://atcoder.jp/contests/abc386/tasks/abc386_c

k = input()
s = list(input())
t = list(input())

if abs(len(s) - len(t)) > 1:
    print("No")
    exit()

if len(t) == len(s):
    diff_cnt = 0
    i = 0
    while i < len(t):
        if s[i] != t[i]:
            diff_cnt += 1
        i += 1
    if diff_cnt > 1:
        print("No")
        exit()
    else:
        print("Yes")
        exit()

elif len(t) == len(s) + 1:
    diff_cnt = 0
    i = 0
    while i < len(s):
        if diff_cnt > 1:
            print("No")
            exit()
        if s[i] != t[i + diff_cnt]:
            diff_cnt += 1
            continue
        i += 1
    print("Yes")
    exit()

elif len(t) == len(s) - 1:
    diff_cnt = 0
    i = 0
    while i < len(t):
        if diff_cnt > 1:
            print("No")
            exit()
        if s[i + diff_cnt] != t[i]:
            diff_cnt += 1
            continue
        i += 1
    print("Yes")
    exit()
