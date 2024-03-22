# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=deque()
        while head:
            a.append(head.val)
            head=head.next
        while a and a[0]==a[-1]:
            a.popleft()
            if a:
                a.pop()
        return len(a)==0