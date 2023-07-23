# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=set()
        x=head
        while x:
            if x in d:
                return x
            d.add(x)
            x=x.next
        return None