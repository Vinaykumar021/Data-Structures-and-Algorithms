class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(img), len(img[0])
        res = [[0] * Cols for _ in range(Rows)]

        for r in range(Rows):
            for c in range(Cols):
                total, count = 0, 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i < 0 or i == Rows or j < 0 or j == Cols:
                            continue
                        total += img[i][j]
                        count += 1
                res[r][c] = total // count

        return res