# https://atcoder.jp/contests/abc376/tasks/abc376_b

n, q = list(map(int, input().split()))

cnt = 0
l = 1
r = 2
for i in range(q):
    h, t_str = input().split()
    t = int(t_str)

    if h == "R":
        tmp1 = r
        tmp_cnt1 = 0
        while True:
            if tmp1 == t:
                break
            if tmp1 == l:
                break
            tmp1 += 1
            if tmp1 == n + 1:
                tmp1 = 1
            tmp_cnt1 += 1

        tmp2 = r
        tmp_cnt2 = 0
        while True:
            if tmp2 == t:
                break
            if tmp2 == l:
                break
            tmp2 -= 1
            if tmp2 == 0:
                tmp2 = n
            tmp_cnt2 += 1

        tmp3 = tmp1 if tmp1 != l else tmp2
        cnt += tmp_cnt1 if tmp3 == tmp1 else tmp_cnt2
        r = t
    elif h == "L":
        tmp1 = l
        tmp_cnt1 = 0
        while True:
            if tmp1 == t:
                break
            if tmp1 == r:
                break
            tmp1 += 1
            if tmp1 == n + 1:
                tmp1 = 1
            tmp_cnt1 += 1

        tmp2 = l
        tmp_cnt2 = 0
        while True:
            if tmp2 == t:
                break
            if tmp2 == r:
                break
            tmp2 -= 1
            if tmp2 == 0:
                tmp2 = n
            tmp_cnt2 += 1

        tmp3 = tmp1 if tmp1 != r else tmp2
        cnt += tmp_cnt1 if tmp3 == tmp1 else tmp_cnt2
        l = t
print(cnt)
