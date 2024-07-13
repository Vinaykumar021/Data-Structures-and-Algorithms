class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total_wealth = 0
        max_wealth = 0
        for i in range(len(accounts)):
            total_wealth = sum(accounts[i])
            max_wealth = max(total_wealth, max_wealth)
        return max_wealth
        