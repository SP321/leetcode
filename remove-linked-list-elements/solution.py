# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans=ListNode(-1,head)
        node=ans
        while node!=None:
            while node.next and node.next.val==val:
                node.next=node.next.next
            node=node.next
        return ans.next