class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        x=-1
        for i in range(n-1,-1,-1):
            y=max(x,arr[i])
            arr[i]=x
            x=y
        return arr
