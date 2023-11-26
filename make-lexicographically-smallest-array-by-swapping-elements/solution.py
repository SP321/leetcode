from sortedcontainers import SortedList
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n=len(nums)
        a=[(x,i) for i,x in enumerate(nums)]
        a.sort()

        values=[i[0] for i in a]+[float('inf')]
        indices=[i[1] for i in a]
        i=0
        for j in range(1,n+1):
            if values[j]-values[j-1]>limit:
                for pos,value in zip(sorted(indices[i:j]),sorted(values[i:j])):
                    nums[pos]=value
                i=j
        return nums

        