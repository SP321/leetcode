class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        strings = [a, b, c]
        ans = a+b+c
        for perm in permutations(strings):
            merged = perm[0]
            for i in range(1,3):
                if perm[i] in merged:
                    continue
                for j in range(len(perm[i])-1,-1,-1):
                    if merged.endswith(perm[i][:j]):
                        merged += perm[i][j:]
                        break
            if len(merged) < len(ans) or (merged < ans and len(merged) == len(ans)):
                ans = merged
        return ans