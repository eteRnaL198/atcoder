s = input().split()

a, b, c = 0, 0, 0
if s[0] == "<":
    b += 1
else:
    a += 1

if s[1] == "<":
    c += 1
else:
    a += 1

if s[2] == "<":
    c += 1
else:
    b += 1

hoge = sorted([a, b, c])[1]
if hoge == a:
    print("A")
elif hoge == b:
    print("B")
elif hoge == c:
    print("C")
