# 最悪なパターンは、右端まで行ってから左端に戻る2N → O(N)
# 5 4 3 2 1 1

n = int(input())
balls = list(map(int, input().split()))

balls_after = [balls[0]]

i = 1
while True:
    if i >= len(balls):
        break

    balls_after.append(balls[i])
    # print(balls, balls_after, i)

    if len(balls_after) < 1:
        # print(balls, balls_after, i)
        i += 1
        continue

    if balls_after[-2] != balls_after[-1]:
        # print(balls, balls_after, i, f"{balls_after[-2]}!={balls_after[-1]}")
        i += 1
        continue

    while len(balls_after) > 1 and balls_after[-2] == balls_after[-1]:
        num = balls_after.pop() + 1  # 一番後ろを取り出す O(1)
        balls_after[-1] = num
        # balls.insert(i + 1, num)  # 挿入したもの以降を前にズラすの計算量がかかる→O(N)
        # print(balls, balls_after, i, f"{num-1}=={num-1}")
    i += 1

print(len(balls_after))
