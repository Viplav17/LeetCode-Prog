class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        word = ""
        if not s:
            return 0

        for ch in s:
            if ch not in word:
                word += ch
            else:
                word = word[word.index(ch) + 1:] + ch

            if len(word) > len(substring):
                substring = word

        return len(substring)
