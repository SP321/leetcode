class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i=0
        c=Counter()
        n=len(nums)
        ans=[]
        for j in range(n):
            c[nums[j]]+=1
            if j-i+1>k:
                c[nums[i]]-=1
                i+=1
            if j-i+1==k:
                take=x
                cur=0
                arr=list(c.most_common())
                for val,ct in sorted(arr,key=lambda x:x[::-1],reverse=True):
                    if take==0:
                        break
                    cur+=val*ct
                    take-=1
                ans.append(cur)
        return ans


