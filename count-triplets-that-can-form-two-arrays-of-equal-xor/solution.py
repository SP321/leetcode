class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        pref=list(accumulate(arr,xor,initial=0))
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if pref[i]==pref[j+1]:
                    ans+=j-i
        return ans