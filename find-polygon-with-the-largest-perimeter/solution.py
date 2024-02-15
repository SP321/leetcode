class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s=0
        c=0
        ans=-1
        for x in nums:
            if c>=2 and x<s:
                ans=x+s
            s+=x
            c+=1
        return ans
        