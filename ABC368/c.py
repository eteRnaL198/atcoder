n = int()
h_s = list(map(int, input().split()))
t = 0
for i in range(n):
    initial_t_reminder = t % 3
    if initial_t_reminder == 0:
        if h_s[i] % 5 == 1:
            t += (h_s[i]//5 )*3 +1
        elif h_s[i] % 5 == 2:
            t += (h_s[i]//5 ) * 

        h_s[i] -= 3
    elif initial_t_reminder == 1:
        pass
    else:

