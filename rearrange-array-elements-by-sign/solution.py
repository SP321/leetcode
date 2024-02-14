class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a,b=[],[]
        for x in nums:
            if x>0:a.append(x)
            else:b.append(x)
        ans=[]
        for i,j in zip(a,b):
            ans.extend([i,j])
        return ans