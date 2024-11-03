# https://atcoder.jp/contests/abc378/tasks/abc378_b

n = int(input())

data = {}
for i in range(n):
    q, r = list(map(int, input().split()))
    data[i + 1] = {"q": q, "r": r}


q = int(input())
for _ in range(q):
    type, today = list(map(int, input().split()))
    quotient = today // data[type]["q"]
    remainder = today % data[type]["q"]
    if remainder <= data[type]["r"]:
        print(quotient * data[type]["q"] + data[type]["r"])
    else:
        print((quotient + 1) * data[type]["q"] + data[type]["r"])
