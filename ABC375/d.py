# https://atcoder.jp/contests/abc375/tasks/abc375_d

s = input()

dict_tmp = {}  # {A: [0, 3], }
for i in range(len(s)):
    if s[i] in dict_tmp:
        dict_tmp[s[i]].append(i)
    else:
        dict_tmp[s[i]] = [i]

dict = {}
for k, v in dict_tmp.items():
    if len(v) > 1:
        dict[k] = v

cnt = 0

for v in dict.values():
    prev = 0
    for i in range(1, len(v)):
        d1 = v[i] - v[i - 1]
        d2 = v[i] - v[i - 1] - 1
        if i == 1:
            cnt += d2
            prev = d2

        else:
            amount = prev + d1 * (i - 1)
            amount += d2
            cnt += amount
            prev = amount

print(cnt)
