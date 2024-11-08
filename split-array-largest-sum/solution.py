class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(sm):
            c=1
            cur=0
            for x in nums:
                if x>sm:
                    return -1
                if cur+x>sm:
                    cur=x
                    c+=1
                else:
                    cur+=x
            return -1 if c>k else 0
        pos=bisect_left(range(10**9),0,key=check,lo=max(nums))
        return pos