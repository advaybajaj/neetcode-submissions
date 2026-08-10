# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find midpoint and split into l1 and l2
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None

        #reverse l2
        revl2 = None
        dummy = l2
        while dummy:
            next_item = dummy.next
            dummy.next = revl2
            revl2 = dummy
            dummy = next_item
        
        #merge list1 and list2
        list1 = l1
        list2 = revl2
        while list2:
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2