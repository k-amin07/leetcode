from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if(not k):
            return False
        seen = {}
        for r in range(len(nums)):
            if(nums[r] in seen):
                if(r - seen[nums[r]] <= k):
                    return True
            seen[nums[r]] = r
            r += 1
        return False

            



sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,1],3))
print(sol.containsNearbyDuplicate([1,2,3,1,2,3],2))
print(sol.containsNearbyDuplicate([99,99],2))
print(sol.containsNearbyDuplicate([1,0,1,1],1))
print(sol.containsNearbyDuplicate([1,2,1],0))
print(sol.containsNearbyDuplicate([0,1,2,3,2,5],3))
print(sol.containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,9],3))
print(sol.containsNearbyDuplicate([1,2,2,3],3))