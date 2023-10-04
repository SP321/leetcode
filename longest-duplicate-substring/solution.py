class Solution:
    def longestDupSubstring(self, s: str) -> str:
        base = 256
        mod = 10**9 - 1

        def rabinKarp(mid, s):
            cur_hash = 0
            for i in range(mid):
                cur_hash = (cur_hash * base + ord(s[i])) % mod

            hashes = {cur_hash: 0}
            baseL = pow(base, mid, mod)

            for pos in range(1, len(s) - mid + 1):
                cur_hash = (cur_hash * base - ord(s[pos-1]) * baseL + ord(s[pos + mid - 1])) % mod
                if cur_hash in hashes:
                    if s[pos:pos+mid] == s[hashes[cur_hash]:hashes[cur_hash]+mid]:
                        return pos
                hashes[cur_hash] = pos

            return -1

        left, right = 1, len(s)
        ans = ""

        while left <= right:
            mid = (left + right) // 2
            pos = rabinKarp(mid, s)
            
            if pos != -1:
                ans = s[pos:pos+mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans