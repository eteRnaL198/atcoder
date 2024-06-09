n_str = input()
n_num = int(n_str)
divider = 998244353

a = 10 ** len(n_str)
sigma = ((a * n_num) - 1) / (a - 1)
print(int((n_num * sigma) % divider))
