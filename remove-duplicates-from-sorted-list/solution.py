# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        node=head
        while node:
            if prev and node.val==prev.val:
                prev.next=node.next
            else:
                prev=node
            node=node.next
        return head