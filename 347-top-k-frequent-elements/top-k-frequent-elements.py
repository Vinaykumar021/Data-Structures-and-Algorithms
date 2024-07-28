class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        defdict = defaultdict(int)
        for num in nums:
            defdict[num] += 1
        return sorted(defdict, key = defdict.get, reverse = True)[:k] 
        