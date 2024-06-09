n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
asc_a = sorted(a)

i = 0
p = []
p_val = 1
skipped = None
while len(p) < n:
    if i >= m:
        if skipped:
            p.append(skipped)
            skipped = None
        else:
            p.append(p_val)
            p_val += 1
    elif skipped and p_val - 1 != asc_a[i]:
        print(p, p_val, asc_a[i], skipped)
        p.append(skipped)
        skipped = None
    elif p_val == asc_a[i]:
        skipped = p_val
        p.append(p_val + 1)
        i += 1
        p_val += 2
    else:
        p.append(p_val)
        p_val += 1
print(p)
