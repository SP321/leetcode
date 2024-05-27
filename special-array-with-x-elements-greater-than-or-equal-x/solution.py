class Solution:
    def specialArray(self, nums: List[int]) -> int:
        c=Counter(nums)
        c[0]=0
        greater=0
        prev=inf
        for x in sorted(c.keys(),reverse=True):
            y=c[x]
            if x<greater<=prev:
                return greater
            greater+=y
            prev=x
        return -1