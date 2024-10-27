# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        res = defaultdict(int)

        def dfs(root, h, maxh):
            if not root: return maxh
            res[root.val] = max(res[root.val], maxh)
            root.left, root.right = root.right, root.left
            return dfs(root.right, h + 1, dfs(root.left, h + 1, max(maxh, h)))

        dfs(root, 0, 0)
        dfs(root, 0, 0)
        return [res[q] for q in queries]