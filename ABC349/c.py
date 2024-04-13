string = input()
code = input().lower()

is_code = True


if code[0] in string and is_code == True:
    idx = string.find(code[0])
    string = string[idx + 1 :]
else:
    is_code = False


if code[1] in string and is_code == True:
    idx = string.find(code[1])
    string = string[idx + 1 :]
else:
    is_code = False


if code[2] == "x" and is_code == True:
    pass
elif code[2] in string and is_code == True:
    pass
else:
    is_code = False

print("Yes" if is_code == True else "No")
