class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans,c=0,0
        for i in  nums:
            if c==0:
                ans=i
            c+= 1 if i==ans else -1
        return ans