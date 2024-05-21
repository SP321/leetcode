class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        for mask in range(1<<n):
            cur=[nums[i] for i in range(n) if (1<<i)&mask]
            ans.append(cur)
        return ans