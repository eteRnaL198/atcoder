n, k = map(int, input().split())
nums = sorted(set(list(map(int, input().split()))))

if nums[0] != 0:
  print(0)
elif k == 1:
  print(1)
else:
  i = 0
  while i+1 < len(nums) and nums[i+1] - nums[i] == 1 and i < k-1:
    i += 1
  mex = nums[i] + 1
  print(mex)
