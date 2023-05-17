# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        single,double=head,head
        prev=None
        while double and double.next:
            double=double.next.next
            tmp=single.next
            single.next=prev
            prev=single
            single=tmp
        ans=0
        while single:
            ans=max(ans,single.val+prev.val)
            single=single.next
            prev=prev.next
        return ans