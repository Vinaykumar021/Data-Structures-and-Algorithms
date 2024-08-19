class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            sum = 0
            for i in piles:
                sum += math.ceil(i/k)
            if sum <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k +1
            
        return res
                    

            
            

        