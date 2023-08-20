class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        graph = {i: set() for i in range(m)}
        indegree_group = {i: 0 for i in range(m)}
        
        group_items = defaultdict(set)
        for i in range(n):
            group_items[group[i]].add(i)
            for j in beforeItems[i]:
                if group[i] != group[j] and group[i] not in graph[group[j]]:
                    graph[group[j]].add(group[i])
                    indegree_group[group[i]] += 1
        
        def topological_sort(graph, indegree):
            result = []
            queue = deque([node for node, degree in indegree.items() if degree == 0])
            while queue:
                v = queue.popleft()
                result.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        queue.append(u)
            return result
        
        sorted_groups = topological_sort(graph, indegree_group)
        if len(sorted_groups) != len(graph):
            return []
        
        ans = []
        for g in sorted_groups:
            x = group_items[g]
            graph_item = defaultdict(set)
            indegree_item = {i: 0 for i in x}
            
            for i in x:
                for j in beforeItems[i]:
                    if j in x and i not in graph_item[j]:
                        graph_item[j].add(i)
                        indegree_item[i] += 1
            
            sorted_items = topological_sort(graph_item, indegree_item)
            if len(sorted_items) != len(x):
                return []
            ans.extend(sorted_items)
        
        return ans