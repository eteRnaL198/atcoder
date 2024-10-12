# https://atcoder.jp/contests/abc374/tasks/abc374_c

n = int(input())
k_arr = sorted(list(map(int, input().split())))

print(k_arr, sum(k_arr))
