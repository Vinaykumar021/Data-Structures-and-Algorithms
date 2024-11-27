class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for w in strs:
            s = ''.join(sorted(w))
            res[s].append(w)
        return list(res.values())