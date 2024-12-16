# https://atcoder.jp/contests/abc383/tasks/abc383_c

import itertools

h, w, d = list(map(int, input().split()))
cells = []
floor_positions = []
for i in range(h):
    row = list(input())
    cells.append(row)
    for j in range(w):
        if cells[i][j] == ".":
            floor_positions.append((i, j))


def calc_mh_d(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


max_v = 2
for positions in itertools.permutations(floor_positions, 2):
    first, second = positions
    sub_total = 2
    for fp in floor_positions:
        if (fp[0] == first[0] and fp[1] == first[1]) or (
            fp[0] == second[0] and fp[1] == second[1]
        ):
            continue
        if calc_mh_d(first, fp) <= d:
            sub_total += 1
        elif calc_mh_d(second, fp) <= d:
            sub_total += 1
    if max_v < sub_total:
        max_v = sub_total
print(max_v)
