class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum_s, sum_t = 0, 0
        for c in s:
            sum_s += ord(c)
        for c in t:
            sum_t += ord(c)
        return chr(sum_t-sum_s)

        