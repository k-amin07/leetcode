class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
        sol = ListNode()
        temp = sol
        if (not list1 and not list2):
            return
        val1 = getattr(list1, 'val', None) if list1 else None
        val2 = getattr(list2, 'val', None) if list2 else None
        while (val1 is not None or val2 is not None):
            if (val2 == None):
                temp.val = val1
                list1 = getattr(list1, 'next', None)
            elif (val1 == None):
                temp.val = val2
                list2 = getattr(list2, 'next', None)
            elif (val2 >= val1):
                temp.val = val1
                list1 = getattr(list1, 'next', None)
            elif (val1 > val2):
                temp.val = val2
                list2 = getattr(list2, 'next', None)
            if (list1 or list2):
                temp.next = ListNode()
                temp = temp.next
            val1 = getattr(list1, 'val', None) if list1 else None
            val2 = getattr(list2, 'val', None) if list2 else None
        return sol

solution = Solution()
# l1 = ListNode(1,ListNode(2,ListNode(4)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))
l1 = ListNode()
l2 = ListNode(0)
solution.mergeTwoLists(l1,l2)