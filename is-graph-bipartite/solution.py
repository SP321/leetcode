class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        s = [0] * len(graph)
        for node in range(len(graph)):
            if s[node] != 0:
                continue
            s[node] = 1
            queue = [node]
            while queue:
                node = queue.pop(0)
                for nei in graph[node]:
                    if s[nei] == 0:
                        queue.append(nei)
                        s[nei] = -s[node]
                    elif s[nei] == s[node]:
                        return False
        return True