class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children[ch]
            node.word = word

        ans = set()

        def dfs(x, y, node):
            if node.word:
                ans.add(node.word)

            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] not in node.children:
                return

            ch = board[x][y]
            board[x][y] = '#'
            dfs(x+1, y, node.children[ch])
            dfs(x-1, y, node.children[ch])
            dfs(x, y+1, node.children[ch])
            dfs(x, y-1, node.children[ch])

            board[x][y] = ch

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

        return list(ans)