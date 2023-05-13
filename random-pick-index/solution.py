class Solution:

    def __init__(self, nums: List[int]):
        self.x={}
        for i in range(len(nums)):
            if nums[i] not in self.x:
                self.x[nums[i]]=[]
            self.x[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.x[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)