# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head = ListNode(0)
        small = small_head

        big_head = ListNode(0)
        big = big_head

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next

            head = head.next
        
        big.next = None
        small.next = big_head.next
        
        return small_head.next