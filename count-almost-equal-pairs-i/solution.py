class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        def check(x,y):
            if x==y:
                return 1
            x=list(str(x))
            for i in range(len(x)):
                for j in range(i+1,len(x)):
                    x[i],x[j]=x[j],x[i]
                    if int(''.join(x))==y:
                        return 1
                    x[i],x[j]=x[j],x[i]
            return 0

        for i in range(n):
            for j in range(i+1,n):
                ans+=check(nums[i],nums[j])|check(nums[j],nums[i])
        return ans