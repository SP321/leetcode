# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t3=head;
        while n>1:
            t3=t3.next
            n-=1
        t1=None
        t2=head
        while t3.next is not None:
            t3=t3.next
            t1=t2
            t2=t2.next
        if t1 is None:
            return head.next
        t1.next=t2.next
        return head