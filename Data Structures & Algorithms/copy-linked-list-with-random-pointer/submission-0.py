"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = dict()
        d[None] = None

        pointer = head
        while pointer:
              d[pointer] = Node(pointer.val)
              pointer = pointer.next
        
        pointer2 = head
        res = Node(0)
        point = res
        while pointer2:
            res.next = d[pointer2]
            res = res.next
            res.random = d[pointer2.random]
            pointer2 = pointer2.next
        
        return point.next