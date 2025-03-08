# https://atcoder.jp/contests/abc395/tasks/abc395_b

n = int(input())

grid = [list("?" * n)] * n
print(grid)

grid[0][0] = "x"
print(grid)


# [] * n はdeep copyにならない
