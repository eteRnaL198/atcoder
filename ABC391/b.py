# https://atcoder.jp/contests/abc391/tasks/abc391_b

n, m = list(map(int, input().split()))
s = []
for i in range(n):
    s.append(list(input()))
t = []
for i in range(m):
    t.append(list(input()))


for i in range(n - m + 1):
    for j in range(n - m + 1):
        flag = True
        for k in range(m):
            for l in range(m):
                if s[i + k][j + l] != t[k][l]:
                    flag = False
                    break
        if flag:
            print(i + 1, j + 1)
            exit()
