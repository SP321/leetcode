# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one,two=head,head
        while two.next and two.next.next:
            two=two.next.next
            one=one.next
        if two.next:
            return one.next
        return one