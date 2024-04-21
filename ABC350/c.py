n = int(input())
nums = list(map(int, input().split()))

dict = {}
for idx, num in enumerate(nums):
    dict[num] = idx


histories = []
for i in range(n):
    if nums[i] == i + 1:
        continue

    j = dict[i + 1]
    dict[nums[i]], dict[nums[j]] = dict[nums[j]], dict[nums[i]]
    nums[i], nums[j] = nums[j], nums[i]
    histories.append([i + 1, j + 1])

length = len(histories)
print(length)
# if length != 0:
if not length:
    for history in histories:
        print(" ".join(map(str, history)))
