class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        i = 0
        while carry and i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
                
            else:
                digits[i] += 1
                carry = 0
                return digits[::-1]
            i += 1
        return [1] + digits