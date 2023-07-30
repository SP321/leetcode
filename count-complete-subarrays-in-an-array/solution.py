class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        s=set(nums)
        ans=0
        for i in range(n):
            a=set()
            for j in range(i,n):
                a.add(nums[j])
                if len(a)==len(s):
                    ans+=1
        return ans