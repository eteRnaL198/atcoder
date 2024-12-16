q = int(input())

queries = []

for _ in range(q):
    n = int(input())
    s = list(input())
    t = list(input())
    queries.append([n, s, t])

answers = []
for qry in queries:
    n, s, t = qry
    i = 0
    flag = True
    while i < n - 4:
        if s[i : i + 4] == ["T", "I", "O", "T"]:
            if not (
                t[i : i + 4] == ["I", "S", "C", "T"]
                or t[i : i + 4] == ["I", "S", "C", "T"]
            ):
                flag = False
                break
            i += 3
        elif s[i : i + 5] == ["T", "I", "O", "T", "I"]:
            if not (
                t[i : i + 5] == ["I", "S", "C", "T", "I"]
                or t[i : i + 5] == ["I", "S", "C", "T"]
            ):
                flag = False
                break
        elif s[i] != t[i]:
            flag = False
            break
        i += 1
    if flag:
        answers.append("Yes")
    else:
        answers.append("No")

print(answers)
