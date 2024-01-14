class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def countSetBits(n):
            ans=0
            for bit_pos in range(n.bit_length()):
                interval = 1 << (bit_pos + 1)
                count = (n + 1) // interval * (interval // 2)
                count += max(0, (n + 1) % interval - interval // 2)
                if (bit_pos+1)%x==0:
                    ans+=count
            return ans
        def bs_right(lo,hi):
            def key_func(val):
                if countSetBits(val)>k:
                    return 1
                else:
                    return 0
            pos= bisect.bisect_right(range(lo,hi),0,key=key_func)
            if pos==hi or key_func(pos-1)!=0:
                return None
            return pos-1
        return bs_right(lo=0,hi=int(343778878348162))