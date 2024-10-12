# https://atcoder.jp/contests/abc374/tasks/abc374_d

import math


def find_closest(arg):
    close_ver = {}
    minimum = 10**10
    for v in vers:
        cur = (v["x"] - arg["x"]) ** 2 + (v["y"] - arg["y"]) ** 2
        if cur < minimum and lines[v["line_idx"]]["drawn"] == False:
            minimum = cur
            close_ver = v
    return close_ver


def calc_d(a, b):
    return math.sqrt((a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2)


n, s, t = list(map(float, input().split()))
lines = []  # {a: {x: y:} c: {x: y:}, drawn: bool}
vers = []  # {x: y: line_idx}
for i in range(int(n)):
    a, b, c, d = list(map(int, input().split()))
    lines.append({"a": {"x": a, "y": b}, "c": {"x": c, "y": d}, "drawn": False})
    vers.append({"x": a, "y": b, "line_idx": i})
    vers.append({"x": c, "y": d, "line_idx": i})


cur_ver = {"x": 0, "y": 0, "line_idx": None}
drawn_count = 0
passed_time = 0
while drawn_count < n:
    # move
    close_ver = find_closest(cur_ver)
    passed_time += calc_d(cur_ver, close_ver) / s

    # draw
    line = lines[close_ver["line_idx"]]
    dest_ver = (
        line["c"]
        if line["a"]["x"] == close_ver["x"] and line["a"]["y"] == close_ver["y"]
        else line["a"]
    )
    cur_ver = dest_ver
    passed_time += calc_d(close_ver, dest_ver) / t
    lines[close_ver["line_idx"]]["drawn"] = True
    drawn_count += 1
print(passed_time)
