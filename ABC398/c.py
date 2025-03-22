# https://atcoder.jp/contests/abc398/tasks/abc398_c

n = int(input())
nums = list(map(int, input().split()))

num_to_labels = {}
for k in range(n):
    if num_to_labels.get(nums[k]):
        num_to_labels[nums[k]].append(k + 1)
    else:
        num_to_labels[nums[k]] = [k + 1]

count = {}
for num in nums:
    if count.get(num):
        count[num] += 1
    else:
        count[num] = 1

filtered_nums = []
for k, v in count.items():
    if v == 1:
        filtered_nums.append(k)

if len(filtered_nums) == 0:
    print(-1)
    exit()
else:
    print(num_to_labels[max(filtered_nums)][0])
