class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for c in s:
            res = res ^ ord(c)
        for c in t:
            res = res ^ ord(c)
        return chr(res)    
        