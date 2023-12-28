class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q=deque()
        i=ans=0
        n=len(nums)
        for j in range(n):
            if nums[j]==0:                    
                q.append(j)
                if len(q)>k:
                    i=q.popleft()+1
            ans=max(ans,j-i+1)
        return ans
