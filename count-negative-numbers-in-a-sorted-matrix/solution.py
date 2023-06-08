class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        cur_r=len(grid[0])-1
        for row in grid:
            l, r = 0, cur_r
            while l <= r:
                mid = (l + r) // 2
                if row[mid] < 0:
                    r = mid - 1
                    cur_r=r
                else:
                    l = mid + 1
            ans += (len(grid[0]) - l)
        return ans 