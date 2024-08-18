a, b, c = list(map(int, input().split()))
if b > c:
    c += 24
    a += 24

if b <= a and a <= c:
    print("No")
else:
    print("Yes")
