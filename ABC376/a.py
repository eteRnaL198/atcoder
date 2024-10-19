# https://atcoder.jp/contests/abc376/tasks/abc376_a

n, c = list(map(int, input().split()))
times = list(map(int, (input().split())))

cnt = 0
prev_time = -c
for t in times:
    if t - prev_time >= c:
        cnt += 1
        prev_time = t
print(cnt)
