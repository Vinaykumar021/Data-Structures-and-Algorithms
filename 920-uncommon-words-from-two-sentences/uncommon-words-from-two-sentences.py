class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split() + s2.split())
        return [w for w, c in count.items() if c == 1]