# https://atcoder.jp/contests/abc386/tasks/abc386_b

import re

disp = input()
print(len(disp) - len(re.findall("00", disp)))
