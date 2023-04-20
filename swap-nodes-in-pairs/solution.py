# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur1=head
        if not cur1:
            return cur1
        newhead=head
        if cur1.next:
            newhead=cur1.next
        prev2=None
        while cur1 and cur1.next :
            cur2=cur1.next
            cur1.next=cur2.next
            cur2.next=cur1
            if prev2:
                prev2.next=cur2
            prev2=cur1
            cur1=cur1.next
        return newhead