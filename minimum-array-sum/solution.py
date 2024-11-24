class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n=len(nums)
        @cache
        def dp(i,op1,op2):
            if i==n:
                return 0
            cur=nums[i]
            ans=dp(i+1,op1,op2)+cur
            if op1>0:
                ans=min(ans,(cur+1)//2+dp(i+1,op1-1,op2))
            if op2>0 and cur>=k:
                ans=min(ans,cur-k+dp(i+1,op1,op2-1))
            if op1>0 and op2>0 and cur>=k:
                if (cur+1)//2>=k:
                    ans=min(ans,((cur+1)//2)-k+dp(i+1,op1-1,op2-1))
                ans=min(ans,(cur-k+1)//2+dp(i+1,op1-1,op2-1))
            return ans
        return dp(0,op1,op2)