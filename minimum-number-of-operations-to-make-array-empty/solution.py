class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        ans=0
        for i in c:
            x=c[i]
            if x<2:
                return -1
            ans+=(x+2)//3
        return ans
        