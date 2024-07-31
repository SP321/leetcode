class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n=len(books)
        dp=[inf]*n
        dp.append(0)
        for i in range(n):
            w,h=0,0
            for j in range(i,n):
                w+=books[j][0]
                if w>shelfWidth:
                    break
                h=max(h,books[j][1])
                dp[j]=min(dp[j],dp[i-1]+h)
        return dp[-2]