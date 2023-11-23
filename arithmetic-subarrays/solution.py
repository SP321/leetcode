class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def helper(x):
            st = set(x)
            if len(x) != len(st):
                return len(st) == 1
            ma, mi, = max(x), min(x)
            if (ma - mi)%(len(x)-1) != 0:
                return False
            for i in range(mi, ma, (ma - mi)//(len(x)-1)):
                if i not in st:
                    return False
            return True
        return [helper(nums[start:stop+1]) for start, stop in zip(l,r)]