# https://atcoder.jp/contests/abc377/tasks/abc377_b

lines = []
for i in range(8):
    lines.append(input())

cnt = 0
for i in range(8):
    for j in range(8):
        flag = True
        if "#" in lines[i]:
            flag = False
        for k in range(8):
            if "#" in lines[k][j]:
                flag = False
        if flag:
            cnt += 1
print(cnt)
