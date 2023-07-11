# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)
        def dfs(node):
            if node.left:
                dfs(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                dfs(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)
        dfs(root)
        ans=[]
        seen=set()
        def dfs2(node,k):
            seen.add(node)
            if k==0:
                ans.append(node.val)
            if k>0:
                for adj in graph[node]:
                    if adj not in seen:
                        dfs2(adj,k-1)
        dfs2(target,k)
        return ans