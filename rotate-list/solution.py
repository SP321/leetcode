# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        tail=head
        n=1
        while tail.next:
            n+=1
            tail=tail.next

        k%=n
        if k==0:
            return head
        k=n-k
        node=head
        prev=None
        for _ in range(k):
            prev=node
            node=node.next
        if prev:
            prev.next=None
            tail.next=head
        return node
        
        
            