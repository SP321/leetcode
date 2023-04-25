class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        x=arr.index(max(arr))
        n=len(arr)
        if x==0 or x==n-1:
            return False
        for i in range(1,x+1)[::-1]:
            if arr[i]<=arr[i-1]:
                return False
        for i in range(x,n-1):
            if arr[i]<=arr[i+1]:
                return False
        return True