class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        a=[(x^k)-x for x in nums]
        b=[x for x in a if x>0]
        return sum(nums)+sum(b) - ( min(abs(x) for x in a) if len(b)%2 else 0 )