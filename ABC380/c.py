# https://atcoder.jp/contests/abc380/tasks/abc380_c

n, k = list(map(int, input().split()))
s = list(input())

distinguished = []
chunk = []
k_one_block_idx = 0
one_block_cnt = 0
for i in range(n):
    if len(chunk) == 0 or chunk[0] == s[i]:
        chunk.append(s[i])
    else:
        distinguished.append("".join(chunk))

        if chunk[0] == "1":
            one_block_cnt += 1
        if chunk[0] == "1" and one_block_cnt == k:
            k_one_block_idx = len(distinguished) - 1

        chunk = [s[i]]

    if i == n - 1:
        distinguished.append("".join(chunk))

        if chunk[0] == "1":
            one_block_cnt += 1
        if chunk[0] == "1" and one_block_cnt == k:
            k_one_block_idx = len(distinguished) - 1

dest_idx = k_one_block_idx - 2
result = []
for i in range(len(distinguished)):
    if i != k_one_block_idx:
        result.append(distinguished[i])
    if i == dest_idx:
        result.append(distinguished[k_one_block_idx])

print("".join(result))
