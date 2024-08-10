class Solution:
    def isValid(self, s: str) -> bool:
        map = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        for c in s:
            if c not in map:
                stack.append(c)
                continue
            elif not stack or map[c] != stack[-1]:
                return False
            stack.pop()

        return not stack
        