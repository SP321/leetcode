class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        prevStack = []
        currStack = []

        for i, num in enumerate(nums):
            while prevStack and nums[prevStack[-1]] < num:
                ans[prevStack.pop()] = num
            decreasingIndices = []
            while currStack and nums[currStack[-1]] < num:
                decreasingIndices.append(currStack.pop())
            while decreasingIndices:
                prevStack.append(decreasingIndices.pop())
            currStack.append(i)

        return ans