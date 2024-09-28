m = int(input())

cnt = 0
shoulder = 10
a = []

while m != 0:
    if m >= 3**shoulder:
        m -= 3**shoulder
        cnt += 1
        a.append(shoulder)
    else:
        shoulder -= 1

print(cnt)
print(" ".join(map(str, a)))
