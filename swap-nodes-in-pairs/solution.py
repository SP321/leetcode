# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                y=head.next
                x=head.next.next
                y.next=head
                head.next=self.swapPairs(x)
                return y
            return head
            
                
            
            
        