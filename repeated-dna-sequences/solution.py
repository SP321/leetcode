class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        char_to_value = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        d = defaultdict(int)
        ans = []
        h = 0
        for i in range(len(s)):
            h = (h << 2) + char_to_value[s[i]]
            h &= (1 << 20) - 1
            if i >= 9:
                if d[h] == 1:
                    ans.append(s[i-9:i+1])
                d[h] += 1
        
        return ans