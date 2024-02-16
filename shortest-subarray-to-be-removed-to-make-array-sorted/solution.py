class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr=[-1]+arr
        n=len(arr)
        i,j=0,n-1
        ans=n-1
        while 1<j and arr[j-1]<=arr[j]:
            j-=1
            
        while i<j and (i==0 or arr[i]>=arr[i-1]):
            r=bisect.bisect_left(arr,arr[i],lo=j)
            ans=min(ans,r-i-1)
            i+=1
        return ans