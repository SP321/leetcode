class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            prev_term = self.countAndSay(n - 1)
            next_term = ''
            i = 0
            while i < len(prev_term):
                count = 1
                while i + 1 < len(prev_term) and prev_term[i] == prev_term[i + 1]:
                    i += 1
                    count += 1
                next_term += str(count) + prev_term[i]
                i += 1
            return next_term