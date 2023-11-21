# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=set()
        y=set()
        node=head
        while node:
            if node.val in x:
                y.add(node.val)
            x.add(node.val)
            node=node.next
        x=sorted(list(x-y))
        head=None
        while x:
            head=ListNode(x.pop(),head)
        return head
            