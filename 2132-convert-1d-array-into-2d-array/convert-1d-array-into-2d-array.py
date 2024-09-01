class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        res = []
        for i in range(m):
            start = i * n
            end = start + n
            res.append(original[start:end])
        return res
        