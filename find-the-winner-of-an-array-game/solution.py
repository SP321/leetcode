class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i=0
        j=1
        while j<len(arr):
            if arr[i]<arr[j]:
                i=j
            j+=1
            if (i==0 and j-i-1==k) or (i!=0 and j-i==k):
                break
        return arr[i]