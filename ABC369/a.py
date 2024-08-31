a, b = sorted(map(int, input().split()))
diff = b - a

s = set()
s.add(a - diff)
if (b - (diff / 2)).is_integer():
    s.add(b - (diff / 2))
s.add(b + diff)
# print(s)
print(len(s))
