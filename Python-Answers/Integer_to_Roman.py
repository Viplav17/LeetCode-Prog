num = 1994

Roman_Map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
solution = ""
change = (10 ** (len(str(num)) - 1))
                
while num > 0:
    digit = num // change
    digit_value = digit * change

 
    num = num % change
    change /= 10

print(solution)

    

        