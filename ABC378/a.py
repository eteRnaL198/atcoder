# https://atcoder.jp/contests/abc378/tasks/abc378_a

balls = list(map(int, input().split()))


cnt = 0
for i in range(4):
    try:
        idx = balls.index(balls[i], i + 1)
    except:
        continue
    if idx != i:
        cnt += 1
        balls.pop(i)
        balls.pop(idx - 1)
        break

if len(balls) == 2:
    if balls[0] == balls[1]:
        print(2)
        exit()
    else:
        print(1)
        exit()

if len(balls) == 4:
    print(0)
