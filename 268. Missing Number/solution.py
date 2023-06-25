from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = int((n/2) * (n+1))
        return total - sum(nums)
