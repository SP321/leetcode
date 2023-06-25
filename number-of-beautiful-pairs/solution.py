class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                first=int(str(nums[i])[:1])
                last=nums[j]%10
                if math.gcd(first,last)==1:
                    ans+=1
        return ans
        