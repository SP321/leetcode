class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n 
        visited = set()
        pathSet = set()
        pathList = []

        def dfs(node):
            if ans[node] != 0:
                dist_to_node = 1
                while pathList:
                    prev_node = pathList.pop()
                    pathSet.remove(prev_node)
                    ans[prev_node] = dist_to_node + ans[node]
                    dist_to_node += 1
                return
            
            if node in pathSet:
                cycle_start_index = pathList.index(node)
                cycle_length = len(pathList) - cycle_start_index
                for i in range(cycle_start_index, len(pathList)):
                    ans[pathList[i]] = cycle_length
                for i in range(0, cycle_start_index):
                    ans[pathList[i]] = cycle_length + (cycle_start_index - i)
                while pathList:
                    pathSet.remove(pathList.pop())
                return

            if node in visited:
                return
            
            visited.add(node)
            pathSet.add(node)
            pathList.append(node)
            dfs(edges[node])

        for i in range(n):
            if i not in visited:
                dfs(i)

        return ans