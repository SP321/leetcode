class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        x = [nums[i] - nums[i - 1] for i in range(1, n)]
        max_len = 0
        window=[]
        for i in x:
            if len(window)==0:
                if i==1:
                    window.append(i)
            elif (window[-1]==1 and i==-1) or (window[-1]==-1 and i==1):
                window.append(i)
            else:
                if i==1:
                    window=[1]
                else:
                    window=[]
            max_len=max(max_len,len(window))
        return max_len+1 if max_len > 0 else -1