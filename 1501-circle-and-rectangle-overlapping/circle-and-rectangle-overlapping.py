class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = xCenter if x1 <= xCenter <= x2 else x1 if xCenter < x1 else x2
        nearest_y = yCenter if y1 <= yCenter <= y2 else y1 if yCenter < y1 else y2
        dist_x = nearest_x - xCenter
        dist_y = nearest_y - yCenter
        return dist_x ** 2 + dist_y ** 2 <= radius ** 2