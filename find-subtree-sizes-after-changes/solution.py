class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(s)
        g=[[] for _ in range(n)]
        for i,x in enumerate(parent):
            if i!=0:
                g[x].append(i)

        height_map=defaultdict(list)
        def dfs(i,h,d={}):
            next_d=d|{s[i]:i}
            height_map[h].append(i)
            if s[i] in d:
                parent[i]=d[s[i]]
            for j in g[i]:
                dfs(j,h+1,next_d)
        dfs(0,0)
        ans=[1]*n
        for x in sorted(height_map.keys(),reverse=True):
            for node in height_map[x]:
                if parent[node]!=-1:
                    ans[parent[node]]+=ans[node]
        return ans