class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = max(last, arr[i])
            arr[i] = last
            last = temp
        return arr