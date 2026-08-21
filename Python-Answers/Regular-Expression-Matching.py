s = "aa"
p = ".*"

n_s = len(s)
n_p = len(p)

pattern = ""
index = 0
last_char = ""

while len(pattern) < n_s and index < n_p:
    if p[index] is None:
        print(False)
        break

    if p[index].isalpha():
        last_char = p[index]
        pattern += p[index]
        index += 1
        continue
    
    if p[index] == "*":
        pattern += last_char
    elif p[index] == ".":
        pattern += s[index]
        last_char = s[index]
        index += 1


if pattern == s:
    print(True)

else:
    print(False)
    
