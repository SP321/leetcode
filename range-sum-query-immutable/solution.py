class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.prefsum=[0]*(n+1)
        for i in range(len(nums)):
            self.prefsum[i+1]=self.prefsum[i]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefsum[right+1]-self.prefsum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)