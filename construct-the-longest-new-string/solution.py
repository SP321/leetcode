class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        dp = dict()
        def dfs(prev: str, x: int, y: int, z: int) -> int:
            if (prev, x, y, z) in dp:
                return dp[(prev, x, y, z)]
            if prev == 'x':
                options = [(y, 'y')]
            elif prev == 'y':
                options = [(x, 'x'), (z, 'z')]
            elif prev == 'z':
                options = [(x, 'x'), (z, 'z')]
            else:
                options = [(x, 'x'), (y, 'y'), (z, 'z')]
            best = 0
            for remaining, next_char in options:
                if remaining > 0:
                    best = max(best, 1 + dfs(next_char, x - (next_char == 'x'), y - (next_char == 'y'), z - (next_char == 'z')))
            dp[(prev, x, y, z)] = best
            return best
        return dfs('', x, y, z)*2
