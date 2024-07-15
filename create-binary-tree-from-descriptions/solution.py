# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        s=set()
        nodes=defaultdict(TreeNode)
        for x,y,z in descriptions:
            s.add(y)
            nodes[y].val=y
            if z:
                nodes[x].left=nodes[y]
            else:
                nodes[x].right=nodes[y]
        root=(set(nodes)-s).pop()
        nodes[root].val=root
        return nodes[root]