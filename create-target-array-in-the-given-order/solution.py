
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans=[]
        for a,b in zip(nums,index):
            ans[b:b]=[a]
        return ans