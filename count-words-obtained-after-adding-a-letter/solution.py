class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        d = set()
        for word in startWords:
            bit_mask = 0
            for i in word:
                bit_mask |= (1 << (ord(i)-ord('a')))
            d.add(bit_mask)
        ans=0
        for word in targetWords:
            bit_mask = 0
            for i in word:
                bit_mask |= (1 << (ord(i)-ord('a')))
            for i in range(26):
                if bit_mask&(1<<i) and (bit_mask-(1<<i)) in d:
                    ans+=1
                    break
        return ans