from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def numbers(self, root, curr=0, nums=[]):
        curr = curr * 10 + root.val
        if(root.left):
            self.numbers(root.left, curr, nums)
        if(root.right):
            self.numbers(root.right, curr, nums)
        if(not(root.left or root.right)):
            nums.append(curr)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        nums = []
        self.numbers(root,0, nums)
        return sum(nums)


root = TreeNode(4,TreeNode(9,TreeNode(5),TreeNode(1)),TreeNode(0))
solution = Solution()
print(solution.sumNumbers(root))