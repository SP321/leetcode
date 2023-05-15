# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        j,y=head,head
        for i in range(k-1):
            j=j.next
        x=j
        while j.next !=None:
            y,j=y.next,j.next
        x.val,y.val=y.val,x.val
        return head