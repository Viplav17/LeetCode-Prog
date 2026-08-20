s = "+-12"
s = s.strip()
sign = 1
solution = 0
step = 0

for char in s:
    if char == "-" and step == 0:
        sign = -1
        Signed = True
        continue
    elif char == "+" and step == 0:
        continue
    elif char == "-" and step != 1:
        print(solution)
        break
    if char.isdigit():
        solution = (solution * 10) + int(char)
        step += 1
        continue
    else:
        print(sign * solution)

print(sign * solution)
