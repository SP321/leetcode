class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        pos_map={}
        for i in range(len(nums)):
            if nums[i] not in pos_map:
                pos_map[nums[i]]=[i]
            else:
                pos_map[nums[i]].append(i)

        @cache
        def dp(i,d,c=2):
            ans=0
            if c>=3:
                ans+=1
            if nums[i]+d in pos_map:
                for j in pos_map[nums[i]+d]:
                    if j>i:
                        ans+=dp(j,d,c+1)
            return ans

        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):             
                ans+=dp(j,nums[j]-nums[i])
        return ans