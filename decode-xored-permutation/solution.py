class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n=len(encoded)
        a=0
        for i in range(1,n+2):
            a ^= i
            if i < n and i % 2 == 1:
                a ^= encoded[i]
        ans=[a]
        for i in encoded:
            ans.append(ans[-1] ^ i)
        return ans