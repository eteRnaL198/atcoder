l, r = list(map(int, input().split()))
if l == 1 and r == 1:
    print("Invalid")
    exit()
if l == 0 and r == 0:
    print("Invalid")
    exit()
if l == 1:
    print("Yes")
    exit()
if r == 1:
    print("No")
    exit()
