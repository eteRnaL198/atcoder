str_n = input()
int_n = int(str_n)

p = 998244353

numerator = pow(10, int_n * len(str_n), p) - 1
denominator = pow(10, len(str_n), p) - 1

ans = (int_n * numerator * pow(denominator, -1, p)) % p

print(ans)
