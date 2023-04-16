import copy

def create_matrix(n):
  matrix = []
  for i in range(n):
    matrix.append(input().split(' '))
  return matrix

def rotate(m):
  new_m = copy.deepcopy(m)
  n = len(m)
  for i in range(n):
    for j in range(n):
      new_m[j][n-1-i] = m[i][j]
  return new_m

def is_equal_one(n, a, b):
  flag = True
  for i in range(n):
    for j in range(n):
      if a[i][j] == '1' and b[i][j] != '1':
        flag = False
  return flag

# main
n = int(input())
A = create_matrix(n)
B = create_matrix(n)
num_sides = 4
i = 0
new_A = copy.deepcopy(A)
while True:
  if i >= num_sides:
    print("No")
    break
  if is_equal_one(n, new_A, B):
    print("Yes")
    break
  new_A = rotate(new_A)
  i += 1
