class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        a=[1]*n
        for _ in range(k):
            for i in range(1,n):
                a[i]+=a[i-1]
                a[i]%=10**9+7
        return a[-1]