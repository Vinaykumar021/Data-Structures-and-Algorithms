class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip().split()
        res = string[-1]
        return len(res)