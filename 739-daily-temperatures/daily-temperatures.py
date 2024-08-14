class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # stack[-1][0] top element first index, stack[0][-1] is bottom or last element last index
                stackTemp, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append((t, i))
        return res
        