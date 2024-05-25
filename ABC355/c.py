n, t = list(map(int, input().split()))
a_arr = [a - 1 for a in list(map(int, input().split()))]

columns = [0] * n
rows = [0] * (n * n)
diags = [0] * 2
turn = 0
for a in a_arr:
    turn += 1

    quo = int(a / n)
    rows[quo] += 1
    if rows[quo] == n:
        print(turn)
        exit()

    rem = a % n
    columns[rem] += 1
    if columns[rem] == n:
        print(turn)
        exit()

    if a % (n + 1) == 0:
        diags[0] += 1
    if diags[0] == n:
        print(turn)
        exit()

    to_left = int(a / n)
    to_top = a % n
    if to_left + to_top == n - 1:
        diags[1] += 1
    if diags[1] == n:
        print(turn)
        exit()


print(-1)
