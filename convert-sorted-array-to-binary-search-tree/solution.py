# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        node= TreeNode()
        node.val=nums[n//2]
        node.left=self.sortedArrayToBST(nums[:n//2])
        node.right=self.sortedArrayToBST(nums[n//2+1:])
        return node