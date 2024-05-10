class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        a=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                a.append([arr[i],arr[j]])
        a.sort(key=lambda x:x[0]/x[1])
        return a[k-1]