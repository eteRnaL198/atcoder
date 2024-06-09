ss = input()

low_count = 0
for s in ss:
    if s.islower():
        low_count += 1

if len(ss) // 2 < low_count:
    print(ss.lower())
else:
    print(ss.upper())
