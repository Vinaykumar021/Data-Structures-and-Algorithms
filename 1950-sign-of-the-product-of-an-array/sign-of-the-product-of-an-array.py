class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_num = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negative_num += 1
        return 1 if negative_num % 2 == 0 else -1
            
        