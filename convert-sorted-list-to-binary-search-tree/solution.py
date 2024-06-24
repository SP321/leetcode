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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        def get_tree(l,r):
            if l==r:
                return None
            m=l+(r-l)//2
            return TreeNode(a[m],get_tree(l,m),get_tree(m+1,r))
        return get_tree(0,len(a))