class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reverseDigits = digits[::-1]
        for i in range(len(reverseDigits)):
            if reverseDigits[i] == 9:
                reverseDigits[i] = 0
            else:
                reverseDigits[i] += 1
                return reverseDigits[::-1]
        return [1] + reverseDigits