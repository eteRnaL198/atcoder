# https://atcoder.jp/contests/abc380/tasks/abc380_a

import re

n = input()
if (
    len(re.findall("1", n)) == 1
    and len(re.findall("2", n)) == 2
    and len(re.findall("3", n)) == 3
):
    print("Yes")
else:
    print("No")
