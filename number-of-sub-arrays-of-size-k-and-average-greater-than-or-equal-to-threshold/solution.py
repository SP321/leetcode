class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=cur=i=0
        n=len(arr)
        for j in range(n):
            cur+=arr[j]
            while j-i+1>k:
                cur-=arr[i]
                i+=1
            if j-i+1==k:
                ans+=cur/k>=threshold
        return ans