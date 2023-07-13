class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for i,j in prerequisites:
            graph[i].append(j)
        
        visited = [False] * numCourses
        stack = [False] * numCourses
        def hasCycle(node):
            visited[node] = True
            stack[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if hasCycle(neighbor):
                        return True
                elif stack[neighbor]:
                    return True
            stack[node] = False
            return False
            
        for i in range(numCourses):
            if not visited[i]:
                if hasCycle(i):
                    return False
        
        return True