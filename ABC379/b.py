# https://atcoder.jp/contests/abc379/tasks/abc379_b

n, k = list(map(int, input().split()))
teeth = list(map(str, input()))

cnt = 0

can_eat = True
healthy_teeth_cnt = 0
i = 0
while True:
    while i < n:
        if teeth[i] == "O":
            healthy_teeth_cnt += 1
        elif teeth[i] == "X":
            healthy_teeth_cnt = 0
        if healthy_teeth_cnt == k:
            for j in range(k):
                teeth[i - j] = "X"
            cnt += 1
            break
        i += 1
    if i == n:
        print(cnt)
        exit(0)
