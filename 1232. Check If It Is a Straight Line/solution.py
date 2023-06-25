from typing import List
class Solution:
    def calculate_slope(self,c0,c1):
        numerator = c1[1] - c0[1]
        denominator = c1[0] - c0[0]
        return float("inf") if denominator == 0 else numerator/denominator

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prev_slope = self.calculate_slope(coordinates[1],coordinates[0])
        for i in range(2,len(coordinates)):
            curr_slope = self.calculate_slope(coordinates[i], coordinates[i-1])
            if(curr_slope!=prev_slope):
                return False
        return True
