n = int(input())
sorted_a = sorted(list(map(int, input().split())), reverse=True)
count = 0
while True:
    sorted_a[0], sorted_a[1] = sorted_a[0] - 1, sorted_a[1] - 1
    if min(sorted_a) < 0:
        break
    count += 1
    sorted_a = sorted(sorted_a, reverse=True)

print(count)
