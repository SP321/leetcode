class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n=len(nums)
        m=len(nums[0])
        x=[sorted(i) for i in nums]

        y=[]
        for i in range(m):
            z=[]
            for j in range(n):
                z.append(x[j][i])
            y.append(z)
        return sum([max(i) for i in y])