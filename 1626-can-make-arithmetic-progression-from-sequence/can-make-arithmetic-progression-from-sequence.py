class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        sequence = True
        n = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sequence = False
            elif arr[i+1] - arr[i] != n:
                sequence = False 

        return sequence



        