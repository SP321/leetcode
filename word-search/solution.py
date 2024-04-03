class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n, m = len(board), len(board[0])
        word_counts = Counter(word)
        word_pos = defaultdict(set)

        for x in range(n):
            for y in range(m):
                char = board[x][y]
                if char in word_counts:
                    word_pos[char].add((x, y))

        if any(len(word_pos[char]) < word_count for char, word_count in word_counts.items()):
            return False
        
        if word_counts[word[0]] > word_counts[word[-1]]:
            word = word[::-1]
    
        def dp(x, y, i):
            if not (0 <= x < n and 0 <= y < m):
                return False

            if board[x][y] != word[i]:
                return False
            
            if i+1 >= len(word):
                return True

            board[x][y] = "#"
            ans = any ([
                dp(x + 1, y, i+1),
                dp(x - 1, y, i+1),
                dp(x, y + 1, i+1),
                dp(x, y - 1, i+1)
            ])
            board[x][y] = word[i]
            return ans
        
        for x, y in word_pos[word[0]]:
            if dp(x, y, 0):
                return True
        
        return False
