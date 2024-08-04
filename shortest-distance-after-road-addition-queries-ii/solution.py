from sortedcontainers import SortedSet
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        sorted_set = SortedSet() 
        for i in range(n):
            sorted_set.add(i)
        result = []
        for x,y in queries:
            pos = sorted_set.bisect_right(x)
            while(sorted_set[pos]<y):
                sorted_set.pop(pos)
            result.append(len(sorted_set)-1)
        return result