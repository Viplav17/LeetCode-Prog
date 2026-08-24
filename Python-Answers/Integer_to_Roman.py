class Solution:
    def intToRoman(self, num: int) -> str:
        Roman_Map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        solution = ""
        change = 10 ** (len(str(num)) - 1)

        def give_Roman(num):
            solution = ""
            track = "I"

            while num != 0:
                for Roman, Value in Roman_Map.items():
                    if num < Value:
                        solution += track
                        num -= Roman_Map[track]
                        track = ""
                        break
                    elif Value == 1000:
                        solution += Roman
                        num -= 1000
                        track = ""
                        break
                    else:
                        track = Roman
                        continue

            return solution

        def give_Roman_4(num):
            solution = ""
            track = "I"

            while num != 0:
                for Roman, Value in Roman_Map.items():
                    if num <= Value:
                        num = Value - num
                        solution = Roman + solution
                        break

            return solution

        while num > 0:
            digit = num // change
            digit_value = digit * change

            if digit == 4 or digit == 9:
                solution += give_Roman_4(digit_value)
            else:
                solution += give_Roman(digit_value)

            num = num % change
            change /= 10

        return solution