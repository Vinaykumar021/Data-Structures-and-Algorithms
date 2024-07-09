class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        minLength = min(len(word1), len(word2))
        for i in range(minLength):
            res.append(word1[i])
            res.append(word2[i])

        res.extend([word1[minLength:], word2[minLength:]])
        return ''.join(res)