class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sol = {}
        for i,j in enumerate(nums):
            if(target-j in sol):
                return [i,sol[target-j]]
            sol[j]=i
solution = Solution()
print(solution.twoSum([2,7,11,15],9))
        