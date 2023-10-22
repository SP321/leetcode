class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        m_l=nums[::]
        m_r=nums[::]
        n=len(nums)
        for i in range(1,n):
            m_l[i]=min(m_l[i],m_l[i-1])
        for i in range(n-2,-1,-1):
            m_r[i]=min(m_r[i],m_r[i+1])
        
        ans=float('inf')
        for i in range(1,n-1):
            a=m_l[i-1]
            b=m_r[i+1]
            x=nums[i]
            if a<x and x>b:
                ans=min(ans,x+a+b)
        return ans if ans!=float('inf') else -1