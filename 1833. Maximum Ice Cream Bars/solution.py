import heapq


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        heapq.heapify(costs)
        count = 0
        while (len(costs)):
            curr = heapq.heappop(costs)
            coins = coins - curr
            if (coins >= 0):
                count = count + 1
            else:
                break
        return count


solution = Solution()

solution.maxIceCream([1,3,2,4,1],7)