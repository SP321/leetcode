# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q=deque([root])
        h=[]
        ans=None
        while q:
            s=0
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                s+=node.val
            heappush(h,s)
            if len(h)>k:
                heappop(h)
        if len(h)==k:
            return h[0]
        return -1
                