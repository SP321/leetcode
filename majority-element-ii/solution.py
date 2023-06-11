class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=defaultdict(int)
        for i in nums:
            c[i]+=1
        ans=[]
        n=len(nums)
        for i in c:
            if c[i]>(n//3):
                ans.append(i)
        return ans