class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=set()
        n=len(arr)
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            if i<0 or i>=n:
                return False
            if arr[i]==0:
                return True
            return dfs(i+arr[i]) or dfs(i-arr[i])
        return dfs(start)