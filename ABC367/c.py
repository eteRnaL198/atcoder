n, k = list(map(int, input().split()))
r = list(map(int, input().split()))

arr = [1] * n

while True:
    if sum(arr) % k == 0:
        print(*arr)

    if arr == r:
        break

    j = len(arr) - 1
    while j >= 0:
        if arr[j] < r[j]:
            arr[j] += 1
            break
        else:
            arr[j] = 1
            j -= 1
