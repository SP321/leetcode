class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k,points,key=lambda a:a[0]**2+a[1]**2)
