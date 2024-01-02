class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c=Counter(nums)
        ans=[]
        while len(c)>0:
            cur=[]
            for i in list(c.keys()):
                cur.append(i)
                c[i]-=1
                if c[i]==0:
                    del c[i]
            ans.append(cur)
        return ans
