n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)

divider = 10**8
i = 0
j = n - 1
count = 0
while i < j:
    if sorted_a[i] + sorted_a[j] >= divider:
        j -= 1
    else:
        count += n - j - 1
        i += 1
rest = n - i - 1  # dividerを超える残りの個数
count += int(((rest + 1) * (rest)) / 2)  # 等差数列の和
print((sum(a) * (n - 1)) - count * divider)
