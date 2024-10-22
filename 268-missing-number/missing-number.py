class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums) + 1):
            sum += i
        res = 0
        for i in range(len(nums)):
            res += nums[i]
        return sum - res

