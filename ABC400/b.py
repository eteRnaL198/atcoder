# https://atcoder.jp/contests/abc400/tasks/abc400_b

n, m = list(map(int, input().split()))

cur = 1
result = 1
for i in range(0, m):
    cur *= n
    result += cur
    if result > pow(10, 9):
        print("inf")
        exit()
print(result)
