class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        cur = 0

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            maxSub = max(cur, maxSub)
        return maxSub