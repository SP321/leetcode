class Solution:
    def findMinHeightTrees(self, n, edges):
        if n==1:
            return [0]
        g, seen = defaultdict(set), [False]*n
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)

        leaves, new_leaves, in_degree = [], [], []
        for i in range(n):
            if len(g[i]) == 1:
                leaves.append(i)
            in_degree.append(len(g[i]))
        while n > 2:
            for leaf in leaves:
                for adj in g[leaf]:
                    in_degree[adj] -= 1
                    if in_degree[adj] == 1:
                        new_leaves.append(adj)
            n -= len(leaves)
            leaves = new_leaves[:]
            new_leaves.clear()
        return leaves