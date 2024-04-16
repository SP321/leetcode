# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,root)
        q=[root]
        for _ in range(depth-2):
            q2=[]
            for node in q:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q=q2
        for node in q:
            node.left=TreeNode(val,node.left,None)
            node.right=TreeNode(val,None,node.right)
        return root
