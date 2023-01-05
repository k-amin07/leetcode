# The problem appears to be analogous to interval scheduling problem, 
# so I'm gonna go with earliest finishing time greedy approach


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # sort by finishing time
        points.sort(key=lambda x: x[1])
        index = 0
        i = 1
        count = 1
        while(i<len(points)):
            if(points[i][0] > points[index][1]):
                count = count + 1
                index = i
            i = i + 1
        return count


solution = Solution()
print(solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))

