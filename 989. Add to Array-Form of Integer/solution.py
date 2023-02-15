class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
       return [int(i) for i in str(int(''.join(map(str,num))) + k)]
       



solution = Solution()
print(solution.addToArrayForm([1,2,0,0],34))
print(solution.addToArrayForm([2,7,4],181))
print(solution.addToArrayForm([9,9,9,9,9,9,9,9,9,9],1))