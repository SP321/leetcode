class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        ans=arr[0]
        c=0
        for i in arr[1:]:
            if i>ans:
                c=1
                ans=i
            else:
                c+=1
            if c==k:
                break
        return ans