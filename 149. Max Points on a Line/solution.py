# This solution has a runtime of 55 ms on leetcode (beats 99.64%). Link to explanation posted on leetcode: https://leetcode.com/problems/max-points-on-a-line/solutions/3021276/python-solution-runtime-beats-99-64/

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if(len(points) == 1):
            return 1
        slopes = [[] for i in range(len(points)-1)]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                num = points[j][1]-points[i][1]
                den = points[j][0]-points[i][0]
                slope = num / den if den != 0 else 'inf'
                slopes[i].append(slope)
        max_freqs = []
        for i in slopes:
            freq = dict()
            for j in i:
                freq[j] = 1 if j not in freq else freq[j] + 1
            max_freqs.append(max(freq.values()) + 1)
        return max(max_freqs)
            
            


solution = Solution()
solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
solution.maxPoints([[0,0]])