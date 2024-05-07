# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num=0
        while head:
            num=num*10+head.val
            head=head.next
        ans=None
        num*=2
        if num==0:
            return ListNode(0)
        while num:
            ans=ListNode(num%10,ans)
            num//=10
        return ans