class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(k):
            oper=maxOperations
            for x in nums:
                oper-=( (x+k-1)//k )-1
                if oper<0:
                    return False
            return True
        return bisect_left(range(10**9+1),True,key=check,lo=1)
