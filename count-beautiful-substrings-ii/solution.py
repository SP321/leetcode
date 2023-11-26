class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        v = 0
        c = 0
        ans = 0
        d = defaultdict(int)
        d[0,0]=1

        valid_squares = set()
        for i in range(k):
            if (i * i) % k == 0:
                valid_squares.add(i)

        for i in range(n):
            if s[i] in "aeiou":
                v += 1
            else:
                c += 1

            diff = v - c
            for q in valid_squares:
                ans += d[diff,(v-q)%k]

            d[diff,v%k]+=1

        return ans