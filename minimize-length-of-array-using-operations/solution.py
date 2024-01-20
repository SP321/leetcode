class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        cur_min=min(nums)
        for x in nums:
            if x%cur_min !=0:
                return 1
        return (nums.count(cur_min)+1)//2