class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        n = len(s)
        mapping = {}
        for i in range(n):
            mapping[s[i]] = i
        res = 0
        for j in range(n):
            index_in_a = mapping[t[j]] 
            res += abs(index_in_a - j)
        return res    

        