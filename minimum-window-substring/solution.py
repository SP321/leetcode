class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c1 = Counter(t)
        c = Counter()
        n = len(s)

        def counter_gte(counter1, counter2):
            for key, value in counter2.items():
                if key not in counter1 or value > counter1[key]:
                    return False
            return True

        ans_right = n
        ans_left = 0
        i=0
        for j in range(n):
            c[s[j]] += 1
            while i <= j and counter_gte(c, c1):
                if j - i  < ans_right-ans_left+1:
                    ans_left = i
                    ans_right = j
                c[s[i]] -= 1
                i += 1

        return s[ans_left:ans_right + 1] if ans_right-ans_left+1 != n + 1 else ""
        