class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        x=defaultdict(lambda:defaultdict(set))
        for a,b,t in meetings:
            g=x[t]
            g[b].add(a)
            g[a].add(b)
        s=set()
        s.add(0)
        s.add(firstPerson)
        for t in sorted(x.keys()):
            cur_graph=x[t]
            visited=set()
            def dfs(u):
                if u in visited:
                    return
                visited.add(u)
                s.add(u)
                for v in cur_graph[u]:
                    dfs(v)
            for a in cur_graph:
                if a in s:
                    dfs(a)
        return list(s)
            




