class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        for relation in relations:
            prev_course, next_course = relation
            graph[prev_course].append(next_course)
        
        @cache
        def dfs(i):
            max_child_time = 0
            for j in graph[i]:
                max_child_time = max(max_child_time, dfs(j))
            
            return max_child_time+time[i-1]

        return max(dfs(i) for i in range(1, n + 1))