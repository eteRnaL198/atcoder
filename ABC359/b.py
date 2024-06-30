n = int(input())
a_arr = list(map(int, input().split()))
result = 0
for i in range(1, (2 * n) - 1):
    if a_arr[i - 1] == a_arr[i + 1]:
        result += 1
print(result)
