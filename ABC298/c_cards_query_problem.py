def execute(box, q, table):
  cmd = q[0]
  if cmd == 1:
    if box.get(str(q[2])):
      box[str(q[2])] = sorted(box[str(q[2])] + [q[1]])
    else:
      box[str(q[2])] = [q[1]]
    if table.get(str(q[1])):
        table[str(q[1])] = sorted(set(table[str(q[1])] + [q[2]]))
    else:
      table[str(q[1])] = [q[2]]
    return [box, table]
  if cmd == 2:
    print(" ".join(map(str, box[str(q[1])])))
    return [box, table]
  if cmd == 3:
    print(" ".join(map(str, table[str(q[1])])))
    return [box, table]

# main
n = int(input())
num_lines = int(input())
queries = []
for _ in range(num_lines):
  queries.append(list(map(int, input().split())))
box = {}
table = {}
for q in queries:
  box, table = execute(box, q, table)
