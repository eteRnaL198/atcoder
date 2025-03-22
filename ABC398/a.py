# https://atcoder.jp/contests/abc398/tasks/abc398_a

import math

n = int(input())

text = ""

if n % 2 == 0:
    for i in range(n):
        text += "=" if i == n / 2 - 1 or i == n / 2 else "-"
else:
    for i in range(n):
        text += "=" if i == math.floor(n / 2) else "-"

print(text)
