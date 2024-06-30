n = int(input())
s = input()

blocks = []  # [[l, r], ...]

i = 0
is_different = False
while i < n:
    next_is_different = i < n - 1 and s[i] != s[i + 1]
    if not is_different and next_is_different:
        blocks.append([i])  # l
    if is_different and not next_is_different:
        blocks[-1].append(i)  # r
    is_different = next_is_different
    i += 1

patterns = []
for b in blocks:
    length = b[1] - b[0] + 1
    pattern = -(-length // 2)  # 切り上げ
    patterns.append(pattern)
print(patterns)

result = 1
for p in patterns:
    result *= p
print(result % (10**9 + 7))
