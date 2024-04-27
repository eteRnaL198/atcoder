a_points = list(map(int, input().split()))
b_points = list(map(int, input().split()))

print(sum(a_points) - sum(b_points) + 1)
