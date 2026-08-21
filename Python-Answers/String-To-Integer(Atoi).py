class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        solution = 0
        step = 0
        
        for char in s:
            if (char == "-" and step == 0):
                sign = -1
                step += 1
                continue
            elif char == "+" and step == 0:
                step += 1
                continue
            elif char == "-" and step != 0:
                break
            
            if char.isdigit():
                solution = (solution * 10) + int(char)
                step += 1
                continue
            else:
                break

        solution *= sign
        if solution < -2**31:
            solution = -2**31
        elif solution > (2**31) - 1:
            solution = 2**31 - 1

        return solution
