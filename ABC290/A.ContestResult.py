n, m = map(int, input().split())
scores = list(map(int, input().split()))
solved = list(map(int, input().split()))

sum = 0
for s in solved:
  sum += scores[s-1]
print(sum)
