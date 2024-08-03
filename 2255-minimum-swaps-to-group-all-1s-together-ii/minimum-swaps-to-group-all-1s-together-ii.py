class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        window_ones = max_window_ones = 0
        total_ones = nums.count(1)
        
        for r in range(2 * n):
            if nums[r % n]:
                window_ones += 1
            if r - l + 1 > total_ones:
                window_ones -= nums[l % n]
                l += 1
            max_window_ones = max(window_ones, max_window_ones)
        return total_ones - max_window_ones
