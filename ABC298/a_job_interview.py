# main
qty = input()
evals = input()
include_o = 'o' in evals
include_x = 'x' in evals
if include_o and not include_x:
  print('Yes')
else:
  print('No')

"""input
4
oo--
"""
"""output
Yes
"""

"""input
3
---
"""
"""output
No
"""
