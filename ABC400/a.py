# https://atcoder.jp/contests/abc400/tasks/abc400_a

a = int(input())

if 400 % a != 0:
    print(-1)
else:
    print(int(400 // a))
