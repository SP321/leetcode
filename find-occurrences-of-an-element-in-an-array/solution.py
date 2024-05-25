class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos=[]
        for i,y in enumerate(nums):
            if y==x:
                pos.append(i)
        ans=[]
        for q in queries:
            if q<=len(pos):
                ans.append(pos[q-1])
            else:
                ans.append(-1)
        return ans