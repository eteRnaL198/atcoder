# https://atcoder.jp/contests/abc391/tasks/abc391_a


d = input()

op = {
    "N": "S",
    "E": "W",
    "W": "E",
    "S": "N",
    "NE": "SW",
    "NW": "SE",
    "SE": "NW",
    "SW": "NE",
}

print(op[d])
