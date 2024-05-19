n = int(input())
names = []
total_rate = 0
for _ in range(n):
    name, rate = input().split()
    names.append(name)
    total_rate += int(rate)
sorted_names = sorted(names)

# num = total_rate % n
# print(sorted_names[num])
print(sorted_names[total_rate % n])
