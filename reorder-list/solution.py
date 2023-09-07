# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        first_half, second_half = head, slow.next
        slow.next = None

        prev, curr = None, second_half
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        second_half = prev
        
        p1, p2 = first_half, second_half
        while p2:
            temp1, temp2 = p1.next, p2.next
            
            p1.next = p2
            p2.next = temp1
            
            p1 = temp1
            p2 = temp2