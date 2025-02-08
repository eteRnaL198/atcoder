# https://atcoder.jp/contests/abc391/tasks/abc391_c

n, q = list(map(int, input().split()))

nest = {}
pigeon_pos = {}
for i in range(1, n + 1):
    pigeon_pos[i] = i
    nest[i] = 1
cnt = 0

for _ in range(q):
    qry = input().split()
    if qry[0] == "2":
        print(cnt)
    if qry[0] == "1":
        pigeon_id = int(qry[1])
        cur_nest_id = pigeon_pos[pigeon_id]
        nest[cur_nest_id] -= 1
        if nest[cur_nest_id] == 1:
            cnt -= 1

        next_nest_id = int(qry[2])
        pigeon_pos[pigeon_id] = next_nest_id
        nest[next_nest_id] += 1
        if nest[next_nest_id] == 2:
            cnt += 1
