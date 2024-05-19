h = int(input())

h_plant = 1
i = 1

while h_plant <= h:
    h_plant += 2**i
    i += 1

print(i)
