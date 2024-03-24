class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        h=[0]
        c=Counter()
        delete_c=Counter()
        ans=[]
        for a,b in zip(nums,freq):
            delete_c[c[a]]+=1
            while h and delete_c[-h[0]]>0:
                delete_c[-heappop(h)]-=1
            c[a]+=b
            heappush(h,-c[a])
            ans.append(-h[0])
        return ans
            