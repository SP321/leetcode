class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort()
        c=Counter(nums)
        sm=sum(nums)
        for x in nums[::-1]:
            c[x]-=1
            cur=sm-x
            if cur%2==0 and c[cur//2]!=0:
                return x
            c[x]+=1
        
                
        