class Solution:
    def minimumCost(self, nums):
        nums.sort()
        pal = lambda x: str(x) == str(x)[::-1]
        left = rght = nums[len(nums)//2]

        while not pal(left): left-= 1
        while not pal(rght): rght+= 1

        return min(sum(map(lambda x: abs(x - left), nums)),
                   sum(map(lambda x: abs(x - rght), nums)))