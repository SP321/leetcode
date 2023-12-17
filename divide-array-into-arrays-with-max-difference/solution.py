class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        cur=[]
        def check(x):
            if x[-1]-x[0]>k:
                    return False
            return True
        for i in nums:
            cur.append(i)
            if len(cur)==3:
                ans.append(cur.copy())
                if not check(cur):
                    return []
                cur=[]
        return ans