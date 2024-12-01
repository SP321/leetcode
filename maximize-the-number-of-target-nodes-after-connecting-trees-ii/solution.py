def exclusive(A, zero, combine, node):
    n = len(A)
    exclusiveA = [zero] * n
    for bit in range(n.bit_length())[::-1]:
        for i in range(n)[::-1]:
            exclusiveA[i] = exclusiveA[i // 2]
        for i in range(n - int(bit==0 and n%2==1)):
            ind = (i >> bit) ^ 1
            exclusiveA[ind] = combine(exclusiveA[ind], A[i], node, i)
    return exclusiveA
 
def rerooter(graph, default, combine, finalize = lambda nodeDP,node,eind: nodeDP):
    n = len(graph)
    rootDP = [0] * n
    forwardDP = [None] * n
    reverseDP = [None] * n
 
    DP = [0] * n
    bfs = [0]
    P = [0] * n
    for node in bfs:
        for nei in graph[node]:
            if P[node] != nei:
                P[nei] = node
                bfs.append(nei)
 
    for node in reversed(bfs):
        nodeDP = default[node]
        for eind, nei in enumerate(graph[node]):
            if P[node] != nei:
                nodeDP = combine(nodeDP, DP[nei], node, eind)
        DP[node] = finalize(nodeDP, node, graph[node].index(P[node]) if node else -1)
    
    for node in bfs:
        DP[P[node]] = DP[node]
        forwardDP[node] = [DP[nei] for nei in graph[node]]
        rerootDP = exclusive(forwardDP[node], default[node], combine, node)
        reverseDP[node] = [finalize(nodeDP, node, eind) for eind, nodeDP in enumerate(rerootDP)]
        rootDP[node] = finalize((combine(rerootDP[0], forwardDP[node][0], node, 0) if n > 1 else default[node]), node, -1)
        for nei, dp in zip(graph[node], reverseDP[node]):
            DP[nei] = dp
    return rootDP, forwardDP, reverseDP

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n=len(edges1)+1
        m=len(edges2)+1
        g=[[] for _ in range(n+m)]
        for u,v in edges1:
            g[u].append(v)
            g[v].append(u)

        g2=[[] for _ in range(n+m)]
        for u,v in edges2:
            g2[u].append(v)
            g2[v].append(u)
        
        def combine(nodeDP, childDP, node, eind):
            oc,ec = nodeDP
            oc2,ec2 = childDP
            return (oc+ec2,ec+oc2)


        ec=0
        oc=0
        def dfs(u,par=None,r=0):
            nonlocal ec,oc
            if r==1:
                oc+=1
            else:
                ec+=1
            for v in g2[u]:
                if v!=par:
                    dfs(v,u,1-r)
        dfs(0)
        c=max(ec,oc)
        default=[(0,1) for _ in range(n)]
        rootDP, forwardDP, reverseDP = rerooter(g, default, combine)
        return [ rootDP[i][1]+c for i in range(n)]