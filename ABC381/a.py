# https://atcoder.jp/contests/abc381/tasks/abc381_a

n = int(input())
s = input()

if n % 2 == 0:
    print("No")
    exit()

for i in range((n + 1) // 2 - 1):
    if s[i] != "1":
        print("No")
        exit()

for i in range((n + 1) // 2 + 1, n - 1):
    if s[i] != "2":
        print("No")
        exit()

print("Yes")
