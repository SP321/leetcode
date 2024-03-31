def helper(a):
    n=len(a)
    minsum = maxsum = a[0][0] + a[0][1]
    minsum_index = maxsum_index = 0
    
    mindiff = maxdiff = a[0][0] - a[0][1]
    mindiff_index = maxdiff_index = 0

    for i in range(1, n):
        sum = a[i][0] + a[i][1]
        diff = a[i][0] - a[i][1]
        
        if sum < minsum:
            minsum = sum
            minsum_index = i
        elif sum > maxsum:
            maxsum = sum
            maxsum_index = i
        
        if diff < mindiff:
            mindiff = diff
            mindiff_index = i
        elif diff > maxdiff:
            maxdiff = diff
            maxdiff_index = i

    if (maxsum - minsum) > (maxdiff - mindiff):
        maximum = maxsum - minsum
        indexes = (minsum_index, maxsum_index)
    else:
        maximum = maxdiff - mindiff
        indexes = (mindiff_index, maxdiff_index)
    
    return maximum, indexes

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int: 
        dist,idx=helper(points)
        ans=dist
        for i in idx:
            d,_=helper(points[:i]+points[i+1:])
            ans=min(ans,d)
        return ans