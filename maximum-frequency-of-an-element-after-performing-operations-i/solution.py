class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        ct=Counter(nums)
        a=sorted(ct.keys())
        b=set()
        for x in a:
            b.add(x)
            b.add(x+k)
            b.add(x-k)
        b=sorted(b)
        sm=0
        i,j=0,0
        n=len(a)
        ans=0
        for target in b:
            while j<n and a[j]-target<=k:
                sm+=ct[a[j]]
                j+=1
            while i<n and target-a[i]>k:
                sm-=ct[a[i]]
                i+=1
            cur=ct[target]
            take=min(numOperations,sm-cur)
            ans=max(ans,cur+take)
        return ans