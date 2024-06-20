class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n-1):
            a = ord(s[i])
            b = ord(s[i+1])
            score = abs(a - b)
            res += score
        return res
        