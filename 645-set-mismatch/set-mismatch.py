class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = Counter(nums)
        duplicate, missing = None, None
        for i in range(1, len(nums) + 1):
            if n[i] == 2:
                duplicate = i
            elif n[i] == 0:
                missing = i
        return [duplicate, missing]
            
