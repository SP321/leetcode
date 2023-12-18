class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        class bs_template:
            def __getitem__(self, x):# return -1  for left invalid, +1 for right invalid 0 for valid.
                print(x)
                if x <= 1:
                    return 0
                s = 0
                for i in range(x // 2):
                    s -= nums[i]
                for i in range(x // 2, x):
                    s += nums[i]
                ret = s + nums[x // 2] * ((x // 2) - (x - (x // 2)))
                for j in range(x, len(nums)):
                    s += nums[j] + nums[j-x] - 2 * nums[j-x+x // 2]
                    ret = min(ret, s + nums[x // 2 + j - x + 1] * ((x // 2) - (x - (x // 2))))
                return 0 if ret <= k else 1

            def __len__(self):
                return 10**18

            def right_valid(self):
                return bisect.bisect_right(self,0,lo=1,hi=n+1)-1
            
            def left_valid(self):
                return bisect.bisect_left(self,0,lo=1,hi=n+1)
            
        temp=bs_template()
        return temp.right_valid()