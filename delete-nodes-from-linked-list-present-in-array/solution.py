# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        a=set(nums)
        ans=ListNode()
        ans.next=head
        node=ans
        while node:
            while node.next and node.next.val in a:
                node.next=node.next.next
            node=node.next
        return ans.next