class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        arrows, last_end = 1, points[0][1]
        
        for point in points[1:]:
            if point[0] > last_end:
                arrows += 1
                last_end = point[1]
        
        return arrows
