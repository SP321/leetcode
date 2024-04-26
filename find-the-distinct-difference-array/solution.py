class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l,r=Counter(),Counter()
        ans=[]
        for x in nums:
            r[x]+=1
        for x in nums:
            l[x]+=1
            r[x]-=1
            if r[x]==0:
                del r[x]
            ans.append(len(l)-len(r))
        return ans