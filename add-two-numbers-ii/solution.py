# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        num2=0
        while l1:
            num1=num1*10+l1.val
            l1=l1.next
        while l2:
            num2=num2*10+l2.val
            l2=l2.next
        x=num1+num2
        ans=ListNode(x%10)
        x//=10
        while x>0:
            temp=ListNode(x%10)
            x//=10
            temp.next=ans
            ans=temp
        return ans

