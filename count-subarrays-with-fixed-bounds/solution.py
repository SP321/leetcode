class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        left_max1=left_max2=None
        left_min=0
        for right,x in enumerate(nums):
            if minK<=x<=maxK:
                if x==minK :
                    left_max1=right
                if x==maxK :
                    left_max2=right
            else:
                left_max1=left_max2=None
                left_min=right+1
            if left_max1 is not None and left_max2 is not None: # found both min and max in [left_min:right]
                left_max=min(left_max1,left_max2)
                #for any left in [left_min:left_max+1] the subarray [left:right] is valid.
                ans+=left_max-left_min+1
        return ans