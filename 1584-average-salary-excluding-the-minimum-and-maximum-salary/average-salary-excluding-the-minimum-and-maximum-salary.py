class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        avg = 0
        count = 0
        if len(salary) == 3:
            return salary[1]
        for i in range(1, len(salary)-1):
            avg += salary[i]
            count = i
        return avg/count
        