# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(n1,n2):
            if not n1:
                return not n2
            if not n2:
                return True
            ans=False
            if n1.val==n2.val:
                ans|=dfs(n1.left,n2.next)
                ans|=dfs(n1.right,n2.next)
            if n2==head:
                ans|=dfs(n1.left,n2)
                ans|=dfs(n1.right,n2)
            return ans
        return dfs(root,head)
