s = "aa"
p = "a"

n_s = len(s)
n_p = len(p)

pattern = ""
index = 0

while len(pattern) <= n_s:
    if p[index] is None:
        print(False)
        break

    
    
