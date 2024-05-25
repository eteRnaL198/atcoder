a, b = list(map(int, input().split()))
arr = [1, 2, 3]
arr.remove(a)
try:
    arr.remove(b)
except:
    print(-1)
else:
    print(arr[0])
