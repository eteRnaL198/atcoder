n, limit = map(int, input().split())
member = list(input())
final_member = []
sum = 0
for i in range(len(member)):
  if member[i] == 'o' and sum < limit:
    final_member.append('o')
    sum += 1
  else:
    final_member.append('x')
print(''.join(final_member))

