class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[0]*n
        m=1
        for i in range(n):
            if i>=m:
                return False
            m=max(m,i+nums[i]+1)
            print(m)
        return True