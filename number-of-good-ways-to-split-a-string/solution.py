class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        r = [0] * n

        st = set()
        for i in range(n - 1, 0, -1):
            st.add(s[i])
            r[i] = len(st)

        st = set()
        ans = 0
        for i in range(n-1):
            st.add(s[i])
            if r[i + 1] == len(st):
                ans += 1

        return ans