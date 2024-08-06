class Solution:
    def minimumPushes(self, word: str) -> int:
        cost = 0
        press = 1

        for i in range(1, len(word)+1):
            cost += press
            if i % 8 == 0:
                press += 1
        return cost


        