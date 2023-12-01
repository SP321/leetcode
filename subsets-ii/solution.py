class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        dups=set()
        for i in range(1<<len(nums)):
            cur=[]
            for j in range(len(nums)):
                if (1<<j)&i:
                    cur.append(nums[j])
            if str(sorted(cur)) not in dups:
                dups.add(str(sorted(cur)))
                ans.append(cur)
        return ans
