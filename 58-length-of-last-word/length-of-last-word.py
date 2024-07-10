class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split()
        length = last_word[-1]
        return len(length)
        