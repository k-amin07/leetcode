import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for i in range(k):
            ele = heapq.heappop(nums)
        return -ele
