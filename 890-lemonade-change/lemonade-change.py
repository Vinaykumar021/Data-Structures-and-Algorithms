class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        count20 = 0
        for i in bills:
            if i == 5:
                count5 += 1
            elif i == 10:
                if count5 > 0:
                    count10 += 1
                    count5 -= 1
                else:
                    return False
            elif i == 20:
                if (count10 >= 1 and count5 >= 1) :
                    count20 += 1
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count20 += 1
                    count5 -= 3
                else:
                    return False

        return True



        