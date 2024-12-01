class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                revL, revR = s[l + 1: r + 1], s[l : r]
                return (revL == revL[::-1] or revR == revR[::-1])
            l+=1
            r-=1
        return True
