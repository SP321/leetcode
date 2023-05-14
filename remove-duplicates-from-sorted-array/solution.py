class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=set()
        i=0
        while i<len(nums):
            if nums[i] in x:
                nums.pop(i)
                i-=1
            x.add(nums[i])
            i+=1
        return len(nums)