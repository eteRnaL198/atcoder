n = int(input())
a = []
a_to_c = {}
a_to_idx = {}
for i in range(n):
    a_val, c_val = list(map(int, input().split()))
    a.append(a_val)
    a_to_idx[a_val] = i
    a_to_c[a_val] = c_val

asc_a = sorted(a)
selected_idx = [a_to_idx[asc_a[-1]]]
i = n - 1
j = n - 2
while j >= 0:
    if a_to_c[asc_a[j]] < a_to_c[asc_a[i]]:
        selected_idx.append(a_to_idx[asc_a[j]])
        i = j
    j -= 1

print(len(selected_idx))
for idx in sorted(selected_idx):
    print(idx + 1, end=" ")
print()
