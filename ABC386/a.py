# https://atcoder.jp/contests/abc386/tasks/abc386_a

nums = sorted(list(map(int, input().split())))

if len(set(nums)) != 2:
    print("No")
    exit()

print("Yes")
