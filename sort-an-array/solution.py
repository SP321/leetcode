class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket = [0]*(10**5+1)
        for x in nums: bucket[x + 5*10**4] += 1
        ans = []
        for i, x in enumerate(bucket, -5*10**4): 
            ans.extend([i]*x)
        return ans 
