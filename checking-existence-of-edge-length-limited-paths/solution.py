class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = [-1] * n
        rank = [0] * n
        o1 = list(range(len(edgeList)))
        o2 = list(range(len(queries)))
        o1.sort(key=lambda x: edgeList[x][2])
        o2.sort(key=lambda x: queries[x][2])
        j = 0
        ans = [False] * len(queries)
        for i in range(len(queries)):
            queryindex = o2[i]
            limit = queries[queryindex][2]

            while j < len(edgeList):
                edgeindex = o1[j]
                if edgeList[edgeindex][2] >= limit:
                    break
                a=edgeList[edgeindex][0]
                b=edgeList[edgeindex][1]
                while parent[a] != -1:
                    a = parent[a]
                while parent[b] != -1:
                    b = parent[b]
                if a != b:
                    if rank[a]>rank[b]:
                        parent[b]=a
                    elif rank[b]>rank[a]:
                        parent[a]=b
                    else:
                        parent[b]=a
                        rank[a]+=1
                j += 1

            p=queries[queryindex][0]
            q=queries[queryindex][1]

            while parent[p] != -1:
                p = parent[p]
            while parent[q] != -1:
                q = parent[q]

            ans[queryindex] = p == q

        return ans

    