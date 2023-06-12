class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        x=[]
        for i in nums:
            if len(x)>0 and x[-1][-1]==i-1:
                x[-1].append(i)
            else:
                x.append([i])
        ans=[]
        for i in x:
            if len(i)==1:
                ans.append(str(i[0]))
            else:
                ans.append(str(i[0])+"->"+str(i[-1]))
        return ans