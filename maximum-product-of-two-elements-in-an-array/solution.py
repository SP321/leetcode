class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx1,mx2=0,0
        for i in nums:
            if i>=mx1:
                mx2=mx1
                mx1=i
            elif i>mx2:
                mx2=i
        return (mx1-1)*(mx2-1)