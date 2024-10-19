# https://atcoder.jp/contests/abc376/tasks/abc376_d

n, m = list(map(int, input().split()))
edge = {}  # {1: [2, 3]}
for i in range(m):
    a, b = list(map(int, input().split()))
    if not edge.get(a):
        edge[a] = [b]
    else:
        edge[a].append(b)


def search(arg_v, cost, costs, visited):
    if arg_v in visited:
        return costs

    if not edge.get(arg_v):
        return costs

    if 1 in edge[arg_v]:
        return cost
    for v in edge[arg_v]:
        costs = []
        if not v in visited:
            costs search(v, cost + 1, costs, visited + [v])
        return costs
    return -1


print(search(1, [], [], []))
