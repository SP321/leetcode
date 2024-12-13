class Solution:
    def findScore(self, nums: List[int]) -> int:
        h=[]
        n=len(nums)
        for i,x in enumerate(nums):
            heappush(h,(x,i))
        cnt=0
        ans=0
        while cnt<n:
            cur,pos=heappop(h)
            if nums[pos]==None:
                continue
            ans+=cur
            for j in [pos-1,pos,pos+1]:
                if 0<=j<n and nums[j]!=None:
                    nums[j]=None
                    cnt+=1
        return ans
