# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer = l1
        carry = 0
        prev = None
        while l1 and l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            add = n1 + n2 + carry

            l1.val = add % 10
            carry = add // 10

            prev = l1
            l1 = l1.next
            l2 = l2.next
            
        while l1 or l2:
            if l2 and (not l1):
                n2 = l2.val
                add = n2 + carry
                
                prev.next = ListNode(add % 10)
                carry = add // 10

                prev = prev.next
                l2 = l2.next
            if l1 and (not l2):
                n1 = l1.val
                add = n1 + carry

                l1.val = add % 10
                carry = add // 10
                
                prev = l1
                l1 = l1.next
        if carry:
            prev.next = ListNode(carry)
        return pointer