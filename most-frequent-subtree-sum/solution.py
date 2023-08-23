# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        ans = Counter()
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            current_sum = node.val + left_sum + right_sum
            ans[current_sum] += 1
            return current_sum
        dfs(root)
        max_count = max(ans.values())
        return [i for i, count in ans.items() if count == max_count]