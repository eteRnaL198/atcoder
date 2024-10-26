# https://atcoder.jp/contests/abc377/tasks/abc377_d

n, m = list(map(int, input().split()))
intervals = []  # {l: 1, r: 2}
for _ in range(n):
    l, r = list(map(int, input().split()))
    intervals.append({"l": l, "r": r})

intervals_asc = sorted(intervals, key=lambda x: (x["l"], x["r"]))

print(intervals_asc)

i = 1
j = 1
k = 0
cnt = 0
while True:
    j = intervals[k]["l"]
    tmp_j = j
    if intervals[k]["l"] == intervals[k]["r"]:
        tmp_j -= 1

    cnt += int((j - i + 1) * (j - i + 1) / 2)

    i = j
    k += 1
