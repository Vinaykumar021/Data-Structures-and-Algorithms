class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashSet1 = set(nums1)
        hashSet2 = set(nums2)

        res = []
        for num in hashSet2:
            if num in hashSet1:
                res.append(num)
        return res
