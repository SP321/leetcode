# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d=set()
        x=head
        while x:
            if x in d:
                return True
            d.add(x)
            x=x.next
        return False