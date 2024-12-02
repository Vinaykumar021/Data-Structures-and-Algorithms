class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for chr in s:
            if chr.isalnum():
                string += chr.lower()
        return string == string[::-1]