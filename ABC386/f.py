# https://atcoder.jp/contests/abc386/tasks/abc386_f

from collections import defaultdict

k = int(input())
s = sorted(list(input()))  # ソートしちゃだめ？
t = sorted(list(input()))

s_map = defaultdict(lambda: 0)
for c in s:
    s_map[c] += 1

t_map = defaultdict(int)
for c in t:
    t_map[c] += 1

all_keys = set(list(s_map.keys()) + list(t_map.keys()))

add_cnt = 0
sub_cnt = 0
for key in all_keys:
    diff = t_map[key] - s_map[key]
    if diff > 0:
        add_cnt += diff
    elif diff < 0:
        sub_cnt += diff


repl_cnt = ((add_cnt + sub_cnt) - abs(add_cnt - sub_cnt)) // 2
total_cnt = repl_cnt + abs(add_cnt - sub_cnt)

if abs(total_cnt) > k:
    print("No")
else:
    print("Yes")
