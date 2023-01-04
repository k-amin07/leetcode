# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        remainder = 0
        sol = ListNode()
        temp = sol
        while (l1 or l2):
            addition = getattr(l1, 'val', 0) + getattr(l2, 'val', 0) + remainder
            remainder = addition // 10 if addition >= 10 else 0
            addition = addition % 10 if addition >= 10 else addition
            temp.val = addition
            l1 = getattr(l1, 'next', None)
            l2 = getattr(l2, 'next', None)
            if (l1 or l2 or remainder):
                temp.next = ListNode()
                temp = temp.next
        if (remainder):
            temp.val = remainder
        return sol


solution = Solution()
l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution.addTwoNumbers(l1,l2)
