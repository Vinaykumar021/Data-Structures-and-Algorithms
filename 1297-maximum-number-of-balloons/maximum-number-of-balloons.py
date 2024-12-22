class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = Counter(text)
        balloon = Counter("balloon")
        res = len(text)
        for c in balloon:
            res = min(res, n[c] // balloon[c])
        return res