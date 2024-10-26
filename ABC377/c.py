# https://atcoder.jp/contests/abc377/tasks/abc377_c

n, m = list(map(int, input().split()))
pieces = []  # {row: 0, col: 1}
for i in range(m):
    row, col = list(map(int, input().split()))
    pieces.append({"row": row, "col": col})


not_placable_squares = {}  # squares[0][1] : bool


def add(row, col, cnt):
    if not_placable_squares.get(row):
        not_placable_squares[row][col] = True
    else:
        not_placable_squares[row] = {col: True}
    return cnt + 1


def check(row, col):
    if row < 1:
        return False
    if row > n:
        return False
    if col < 1:
        return False
    if col > n:
        return False

    if not_placable_squares.get(row) and not_placable_squares[row].get(col):
        return False
    return True


count = 0

for p in pieces:
    count = add(p["row"], p["col"], count)

for p in pieces:
    if check(p["row"] + 2, p["col"] + 1):
        count = add(p["row"] + 2, p["col"] + 1, count)
    if check(p["row"] + 1, p["col"] + 2):
        count = add(p["row"] + 1, p["col"] + 2, count)
    if check(p["row"] - 1, p["col"] + 2):
        count = add(p["row"] - 1, p["col"] + 2, count)
    if check(p["row"] - 2, p["col"] + 1):
        count = add(p["row"] - 2, p["col"] + 1, count)
    if check(p["row"] - 2, p["col"] - 1):
        count = add(p["row"] - 2, p["col"] - 1, count)
    if check(p["row"] - 1, p["col"] - 2):
        count = add(p["row"] - 1, p["col"] - 2, count)
    if check(p["row"] + 1, p["col"] - 2):
        count = add(p["row"] + 1, p["col"] - 2, count)
    if check(p["row"] + 2, p["col"] - 1):
        count = add(p["row"] + 2, p["col"] - 1, count)

print(n * n - count)
