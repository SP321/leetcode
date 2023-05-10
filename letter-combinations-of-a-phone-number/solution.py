class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a = [''] * 10
        c = ord('a')
        for i in range(2, 10):
            for _ in range(4 if i in [7, 9] else 3):
                a[i] += chr(c)
                c += 1
        ans = []
        x = digits
        n = len(digits)

        def get_combinations(i, prefix):
            if i == n:
                ans.append(prefix)
            else:
                for ch in a[int(x[i])]:
                    get_combinations(i+1, prefix+ch)

        if n > 0:
            get_combinations(0, "")
        return ans
