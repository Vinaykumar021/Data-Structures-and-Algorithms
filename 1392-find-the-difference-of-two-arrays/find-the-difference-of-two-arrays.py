class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1, n2 = set(nums1), set(nums2)
        res1, res2 = [], []
        for num in n1:
            if num not in n2:
                res1.append(num)
        for num in n2:
            if num not in n1:
                res2.append(num)
        return [res1, res2]
        