class Solution:
    def reverse(self, x: int) -> int:
        revInteger = int(str(abs(x))[::-1])
        if revInteger.bit_length() > 31:
            return 0
        if x < 0:
            return -revInteger
        else:
            return revInteger