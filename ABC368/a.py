n, k = map(int, input().split())
i = list(map(int, input().split()))
print(*i[n - k :] + i[: n - k])
