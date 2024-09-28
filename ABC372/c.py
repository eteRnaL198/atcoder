n, q = list(map(int, input().split()))
s = input()
queries = []  # {idx, alt}
for i in range(q):
    idx_str, alt = input().split()
    idx = int(idx_str) - 1
    queries.append({"idx": idx, "alt": alt})

cur_cnt = s.count("ABC")
s_arr = list(s)
for query in queries:
    left = query["idx"] - 2 if query["idx"] - 2 > 0 else 0
    right = query["idx"] + 3 if query["idx"] + 3 < n else n
    before_cnt = "".join(s_arr[left:right]).count("ABC")
    replaced_target = (
        s_arr[left : query["idx"]] + [query["alt"]] + s_arr[query["idx"] + 1 : right]
    )
    after_cnt = "".join(replaced_target).count("ABC")
    s_arr[query["idx"]] = query["alt"]
    cur_cnt = cur_cnt + after_cnt - before_cnt
    print(cur_cnt)
