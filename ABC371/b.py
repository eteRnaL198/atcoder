n, m = list(map(int, input().split()))
babies = []
for _ in range(n):
    babies.append([])

for _ in range(m):
    tmp = input().split()
    fam_id = int(tmp[0]) - 1
    gend = tmp[1]

    if "M" not in babies[fam_id] and gend == "M":
        print("Yes")
    else:
        print("No")

    babies[fam_id].append(gend)
