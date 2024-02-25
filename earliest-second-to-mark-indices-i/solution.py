class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n=len(nums)
        def possible(k):
            c=0
            pos=defaultdict(lambda:n)
            for i,x in enumerate(changeIndices[:k]):
                pos[x]=i
            order=list(range(1,n+1))
            order.sort(key=lambda x:pos[x])
            j=0
            for i,x in enumerate(changeIndices[:k]):
                if x==order[j] and nums[x-1]<=c:
                        c-=nums[x-1]
                        j+=1
                else:
                    c+=1
                if j==n:
                    return True
            return False
        m=len(changeIndices)
        def key_func(k):
            if possible(k):
                return 0
            else:
                return -1
        pos=bisect.bisect_left(range(1,m+1),0,key=key_func)
        if pos==m+1 or key_func(pos+1)!=0:
            return -1
        return pos+1
