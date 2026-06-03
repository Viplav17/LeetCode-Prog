class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        array = list(map(int, str(x)))
        
        n = len(array)
        mid = n // 2

        count = 2 if n % 2 != 0 else 1

        for i in range(mid+count-1, n):
            if array[i] != array[i-count]:
                return False
            count += 2
        return True
