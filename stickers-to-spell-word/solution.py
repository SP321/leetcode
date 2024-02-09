class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        ss=set(target)
        @cache
        def dp(c):
            if sum(c)==0:
                return 0
            ans=inf
            for sticker in stickers:
                new_c=tuple(max(0,c[i]-sticker.count(ch)) for i,ch in enumerate(ss))
                if new_c!=c:
                    ans=min(ans,1+dp(new_c))
            return ans
        ans = dp(tuple(target.count(i) for i in ss))
        return ans if ans < inf else -1