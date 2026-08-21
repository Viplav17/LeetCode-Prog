s = "aa"
p = "a*"

n_s = len(s)
n_p = len(p)

pattern = ""
index = 0
last_char = ""

while len(pattern) <= n_s:
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

    
    
