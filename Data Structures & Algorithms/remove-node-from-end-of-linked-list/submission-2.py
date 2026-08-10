# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pointer1 = dummy
        pointer2 = dummy
        while n > 0:
            pointer2 = pointer2.next
            n-=1
        while pointer2.next:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        pointer1.next = pointer1.next.next
        return dummy.next