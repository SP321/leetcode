class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans=[]
        def check(a):
            for x,y in pairwise(a):
                if x!=y-1:
                    return False
            return True
        for i in range(n):
            if i+k<=n:
                cur=nums[i:i+k]
                if check(cur):
                    ans.append(cur[-1])
                else:
                    ans.append(-1)
        return ans