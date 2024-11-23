class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        queries=deque(sorted(queries))
        h=[]
        cur=0
        c=[0]*(n+1)
        ans=len(queries)
        for i,x in enumerate(nums):
            cur+=c[i]
            while queries and queries[0][0]<=i:
                l,r=queries.popleft()
                heappush(h,-r)
            while cur<x and h:
                r=-heappop(h)
                if r<i:
                    return -1
                ans-=1
                cur+=1
                c[r+1]-=1
            if cur<x:
                return -1
        return ans