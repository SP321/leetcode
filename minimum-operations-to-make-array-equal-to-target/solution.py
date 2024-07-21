class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        sign  = lambda x:x<0
        prev = 0
        ans=0
        for i in range(len(nums)):
            cur=target[i]-nums[i]
            if sign(prev)!=sign(cur):
                prev=0
            ans+=max(0,abs(cur)-abs(prev))
            prev=cur
        return ans