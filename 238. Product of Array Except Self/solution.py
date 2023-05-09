from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1): 
            # range(start,stop,step): start at len(nums) -1 which is the last index, stop at 0, take a negative step each time
            res[i]*=postfix
            postfix *= nums[i]
        return res
    
solution = Solution()
solution.productExceptSelf([1,2,3,4])
            