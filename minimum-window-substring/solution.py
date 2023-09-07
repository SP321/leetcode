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

        minl = n + 1
        ans_right = 0
        ans_left = 0
        j = 0
        for i in range(n):
            c[s[i]] += 1
            while j <= i and counter_gte(c, c1):
                if i - j  < minl:
                    minl = i - j
                    ans_left = j
                    ans_right = i
                c[s[j]] -= 1
                j += 1

        return s[ans_left:ans_right + 1] if minl != n + 1 else ""
        