# https://atcoder.jp/contests/abc381/tasks/abc381_c

n = int(input())
s = list(input())

max_len = 1

chunks = []
cur_chunk = []
for c in s:
    if (
        c == "/"
        or (c == "1" and len(cur_chunk) > 0 and cur_chunk[0] != "1")
        or (c == "2" and len(cur_chunk) > 0 and cur_chunk[0] != "2")
    ):
        if len(cur_chunk) > 0:
            chunks.append("".join(cur_chunk))
        cur_chunk = []
        cur_chunk.append(c)
    elif (
        c == "1"
        and (len(cur_chunk) == 0 or (len(cur_chunk) > 0 and cur_chunk[0] == "1"))
    ) or (
        c == "2"
        and (len(cur_chunk) == 0 or (len(cur_chunk) > 0 and cur_chunk[0] == "2"))
    ):
        cur_chunk.append(c)

# print(chunks)

for i in range(len(chunks) - 3):
    if chunks[i][0] != "1" or chunks[i + 1][0] != "/" or chunks[i + 2][0] != "2":
        continue

    shorter_len = (
        len(chunks[i]) if len(chunks[i]) < len(chunks[i + 2]) else len(chunks[i + 2])
    )
    cur_len = shorter_len * 2 + 1
    max_len = cur_len if cur_len > max_len else max_len
    # print(chunks[i], chunks[i + 1], chunks[i + 2], shorter_len, max_len)

print(max_len)
