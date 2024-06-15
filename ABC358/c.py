n, m = list(map(int, input().split()))
stands = []
for _ in range(n):
    stands.append(input())

min = n

for i in range(1, pow(2, n)):
    binary = format(i, "0" + n + "b")
    # print(binary)
    flavor_count = [0] * m
    for j in range(len(binary)):
        if binary[j] == "0":
            continue
        if binary[j] == "1":
            for k in range(m):
                if stands[j][k] == "o":
                    flavor_count[k] += 1
    # print(flavor_count)
    if 0 in flavor_count:
        continue

    stands_count = binary.count("1")
    if stands_count < min:
        min = stands_count

print(min)
