# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l,r=list1,list1
        for _ in range(a-1):
            l=l.next
        for _ in range(b):
            r=r.next
            
        l.next=list2
        while l.next:
            l=l.next
        l.next=r.next
        return list1