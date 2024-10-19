class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        sz=1
        for _ in range(n):
            sz=sz*2+1
        k-=1
        bit=0
        while sz:
            mid=sz//2
            if k>mid:
                bit^=1
                diff=k-mid
                k=mid-diff
            elif k==sz//2:
                if sz>1:
                    bit^=1
                return str(bit)
            sz=sz//2
