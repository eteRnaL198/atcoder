n = int(input())

if n == 0:
    print("#")
    exit()

unit = ["###", "#.#", "###"]
if n == 1:
    print("\n".join(unit))
    exit()

row1 = []
row2 = []
row3 = []
for i in range(len(unit)):
    row1.append(unit[i] * 3)
    row2.append(unit[i] + "." * 3 + unit[i])
    row3.append(unit[i] * 3)
if n == 2:
    print("\n".join(row1))
    print("\n".join(row2))
    print("\n".join(row3))
    exit()

unit = row1 + row2 + row3
row1 = []
row2 = []
row3 = []
for i in range(len(unit)):
    row1.append(unit[i] * 3)
    row2.append(unit[i] + "." * 3 * 3 + unit[i])
    row3.append(unit[i] * 3)
if n == 3:
    print("\n".join(row1))
    print("\n".join(row2))
    print("\n".join(row3))
    exit()

unit = row1 + row2 + row3
row1 = []
row2 = []
row3 = []
for i in range(len(unit)):
    row1.append(unit[i] * 3)
    row2.append(unit[i] + "..." * 3 * 3 + unit[i])
    row3.append(unit[i] * 3)
if n == 4:
    print("\n".join(row1))
    print("\n".join(row2))
    print("\n".join(row3))
    exit()


unit = row1 + row2 + row3
row1 = []
row2 = []
row3 = []
for i in range(len(unit)):
    row1.append(unit[i] * 3)
    row2.append(unit[i] + "..." * 3 * 3 * 3 + unit[i])
    row3.append(unit[i] * 3)
if n == 5:
    print("\n".join(row1))
    print("\n".join(row2))
    print("\n".join(row3))
    exit()


unit = row1 + row2 + row3
row1 = []
row2 = []
row3 = []
for i in range(len(unit)):
    row1.append(unit[i] * 3)
    row2.append(unit[i] + "..." * 3 * 3 * 3 * 3 + unit[i])
    row3.append(unit[i] * 3)
if n == 6:
    print("\n".join(row1))
    print("\n".join(row2))
    print("\n".join(row3))
    exit()
