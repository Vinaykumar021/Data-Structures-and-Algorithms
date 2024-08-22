class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            #left sorted portion
            if nums[mid] >= nums[l]:
                if nums[l] > target or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            #right sorted portion
            else:
                if nums[r] < target or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1




                
            


        