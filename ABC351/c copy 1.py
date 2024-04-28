# 最悪なパターンは、右端まで行ってから左端に戻る2N → O(N)
# 5 4 3 2 1 1

# 同じ数字の1つ先まで足してから振り返る
# そしたら影響が無い
# 後戻りが無くなる
# 同じだった瞬間に戻ると、その先でまた同じだったときに後戻りする

n = int(input())
balls = list(map(int, input().split()))

balls_after = [balls[0]]

i = 1
while True:
    print(balls, balls_after, i)
    if i >= len(balls):
        break

    if len(balls_after) < 1:
        balls_after.append(balls[i])
        print(balls, balls_after, i)
        i += 1
        continue

    if balls_after[-1] != balls[i]:
        balls_after.append(balls[i])
        print(balls, balls_after, i)
        i += 1
        continue

    if balls_after[-1] == balls[i]:
        num = balls_after.pop() + 1
        balls.insert(i + 1, num)
        print(balls, balls_after, i)
        i += 1

print(len(balls_after))
