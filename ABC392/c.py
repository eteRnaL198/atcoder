# https://atcoder.jp/contests/abc392/tasks/abc392_c

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))


q2p = {}
for i in range(n):
    q2p[q[i]] = p[i]

prsn2q = {}
for i in range(n):
    prsn2q[i + 1] = q[i]

for i in range(1, n + 1):
    prsn_id = q2p[i]
    print(prsn2q[prsn_id], end=" ")
print()
