# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        a=ListNode()
        b=ListNode()
        c=a
        d=b
        cur=head
        fl=True
        while cur:
            if fl:
                c.next=cur
                c=c.next
            else:
                d.next=cur
                d=d.next
            cur=cur.next
            fl=not fl
        d.next=None
        c.next=b.next
        return a.next
        
