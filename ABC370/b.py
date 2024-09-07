n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

elem = a[0][0]
if n == 1:
    print(elem)
    exit()

for i in range(2, n + 1):
    if elem >= i:
        elem = a[elem - 1][i - 1]
    elif elem < i:
        elem = a[i - 1][elem - 1]
print(elem)
