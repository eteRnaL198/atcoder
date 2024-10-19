# https://atcoder.jp/contests/abc376/tasks/abc376_c

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

t_sizes = sorted(a, reverse=True)
b_sizes = sorted(b, reverse=True)

t_idx = 0
b_idx = 0
remainder_t_sizes = []
while True:
    if t_idx >= n:
        break
    if b_idx >= n - 1:
        remainder_t_sizes.append(t_sizes[-1])
        break

    if t_sizes[t_idx] <= b_sizes[b_idx]:
        t_idx += 1
        b_idx += 1
    else:
        remainder_t_sizes.append(t_sizes[t_idx])
        t_idx += 1

if len(remainder_t_sizes) >= 2:
    print(-1)
    exit()

print(remainder_t_sizes[0])
