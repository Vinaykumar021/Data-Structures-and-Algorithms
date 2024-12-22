class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        b = Counter("balloon")
        res = len(text)
        for i in b:
            res = min(res, c[i] // b[i])
        return res