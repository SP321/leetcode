class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        s = sum(batteries)
        batteries.sort()
        while batteries and batteries[-1] > s // n:
            s -= batteries.pop()
            n -= 1
        return s // n