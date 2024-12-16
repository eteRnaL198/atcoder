# https://atcoder.jp/contests/abc383/tasks/abc383_a

n = int(input())
t, v = list(map(int, input().split()))
amount = v
current_t = t

for _ in range(n - 1):
    t, v = list(map(int, input().split()))
    amount -= t - current_t
    if amount < 0:
        amount = 0
    amount += v
    current_t = t


print(amount)
