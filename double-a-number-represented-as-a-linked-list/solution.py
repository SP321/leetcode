# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        while head:
            num = num * 10 + head.val
            head = head.next
        num *= 2
        dummy = ListNode(0)
        tail = dummy
        
        if num == 0:
            return ListNode(0)

        while num:
            num, val = divmod(num, 10)
            node = ListNode(val)
            node.next = dummy.next
            dummy.next = node

        return dummy.next