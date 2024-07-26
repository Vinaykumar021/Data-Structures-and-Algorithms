class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value = False
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                value = True
        return value
        