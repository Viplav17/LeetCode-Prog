class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        n = len(s)
        solution = []
        Row = 1
        Row_Count = 1
        Row_Change = 1
        index = 0

        while len(solution) != n:
            if index == n:
                index = 0
                Row += 1
                Row_Change = 1
                Row_Count = 1

            if Row == Row_Count:
                solution.append(s[index])

            if Row_Count == numRows:
                Row_Change = -1
            elif Row_Count == 1:
                Row_Change = 1

            Row_Count += Row_Change
            index += 1

        return "".join(solution)