# https://atcoder.jp/contests/abc400/tasks/abc400_c

# 10^18 ≒ 2^60

n = int(input())
cnt = 0

a = 1
b = 1
po2 = pow(2, a)
squared = pow(b, 2)

while True:

    po2 = pow(po2, 2)
