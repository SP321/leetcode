class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        nums.append(0)
        cur_req_k=0
        ans=0
        i=0
        for j in range(n):
            diff=nums[j]-nums[j-1]
            cur_req_k+=(j-i)*diff
            while i<j and cur_req_k>k:
                cur_req_k-=nums[j]-nums[i]
                i+=1
            ans=max(ans,j-i+1)
        return ans