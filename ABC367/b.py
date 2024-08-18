x = input()
i = len(x) - 1
while x[i] == "0" and x[i] != ".":
    i -= 1
if x[i] == ".":
    print(x[:i])
else:
    print(x[: i + 1])
