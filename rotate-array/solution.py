class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        x=nums+nums
        for i in range(n):
            nums[i]=x[(i+n-k)%n]