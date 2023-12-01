class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(1<<len(nums)):
            cur=[]
            for j in range(len(nums)):
                if (1<<j)&i:
                    cur.append(nums[j])
            ans.append(cur)
        return ans
