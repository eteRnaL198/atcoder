s = input()
r_i = 0
m_i = 0
for i in range(len(s)):
    if s[i] == "R":
        r_i = i
    elif s[i] == "M":
        m_i = i

if r_i < m_i:
    print("Yes")
else:
    print("No")
