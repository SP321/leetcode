class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        or_all=reduce(lambda x,y:x|y,nums)
        for j in range(30, -1, -1):
            c = 0
            cur = or_all
            new_mask=~((ans&or_all) | ((1 << j) - 1))
            for x in nums:
                cur &= x
                if cur &new_mask ==0:
                    c += 1
                    cur = or_all
            if n - c > k:
                ans |= 1 << j
        return ans