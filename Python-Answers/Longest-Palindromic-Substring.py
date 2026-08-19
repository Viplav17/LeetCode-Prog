class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        solution = ""
        temp_solution = solution

        mid_index = n // 2
        count = 1

        for index in range(n):
            temp_solution = s[index]
            count = 1
            while index >= count and index + count < n:
                if s[index + count] == s[index - count]:
                    temp_solution = s[index + count] + temp_solution + s[index + count]
                    count += 1
                else:
                    break

            if len(temp_solution) > len(solution):
                solution = temp_solution

            count = 0
            while index >= count and index + count < n - 1:
                if s[index + count + 1] == s[index - count]:
                    if count == 0:
                        temp_solution = s[index + count] + s[index + count + 1]
                        count += 1
                    else:
                        temp_solution = s[index - count] + temp_solution + s[index + count + 1]
                        count += 1
                else:
                    break

            if len(temp_solution) > len(solution):
                solution = temp_solution

        return solution