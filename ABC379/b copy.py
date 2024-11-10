# https://atcoder.jp/contests/abc379/tasks/abc379_b

n, k = list(map(int, input().split()))
teeth = input()

cnt = 0

can_eat = True
while can_eat:
    cht = teeth.split("X")
    for i in range(len(cht)):
        if len(ht) >= k:
            can_eat = True
    if can_eat:
        cnt += 1


print(teeth)
