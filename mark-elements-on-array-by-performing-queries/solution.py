class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total=sum(nums)
        h=[(x,i) for i,x in enumerate(nums)]
        heapq.heapify(h)
        marked=set()
        ans=[]
        for pos,k in queries:
            if pos not in marked:
                marked.add(pos)
                total-=nums[pos]
            c=0
            while c<k and h:
                x,i=heapq.heappop(h)
                if i not in marked:
                    c+=1
                    marked.add(i)
                    total-=nums[i]
            ans.append(total)
        return ans