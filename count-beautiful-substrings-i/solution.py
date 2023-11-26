class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        v = 0
        c = 0
        ans = 0
        d = defaultdict(list)
        d[0].append(-1)

        for i in range(n):
            if s[i] in "aeiou":
                v += 1
            else:
                c += 1

            diff = v - c
            if diff in d:
                for start in d[diff]:
                    dist=(i-start)
                    if dist%2==0 and ((dist/2)*(dist/2))% k == 0:
                        ans += 1

            d[diff] .append(i)

        return ans