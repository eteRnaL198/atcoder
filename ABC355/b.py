n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c_arr = sorted(a + b)
cnt = 0
for c in c_arr:
    if c in a:
        cnt += 1
        if cnt == 2:
            print("Yes")
            exit()
    else:
        cnt = 0
print("No")
