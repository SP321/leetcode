class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c=Counter(arr)
        ans=len(c)
        for x in c.most_common()[::-1]:
            if x[1]>k:
                break
            k-=x[1]
            ans-=1
        return ans