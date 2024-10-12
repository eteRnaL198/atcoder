# https://atcoder.jp/contests/abc375/tasks/abc375_a

n = int(input())
seats = input()

cnt = 0
for i in range(n):
    print(seats[:100])
    if "#.#" == seats[i : i + 3]:
        cnt += 1
print(cnt)
