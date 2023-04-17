class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        ans=[]
        for i in sorted(c.items(),key=lambda x:-x[1])[0:k]  :
            ans.append(i[0])
        return ans
            
