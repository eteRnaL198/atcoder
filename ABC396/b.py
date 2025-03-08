# https://atcoder.jp/contests/abc396/tasks/abc396_b

q = int(input())

stack = [0] * 100

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2:
        print(stack.pop(-1))
