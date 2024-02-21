from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result: ListNode

        if list1.val <= list2.val:
            result = list1
            list1 = list1.next

        return result


test = Solution().mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4])
print(test)
