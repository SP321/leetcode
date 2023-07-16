class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None]*26
            self.end_of_word = False

    def insert(self, root, word):
        node = root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = self.TrieNode()
            node = node.children[index]
        node.end_of_word = True

    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        root = self.TrieNode()
        for fword in forbidden:
            self.insert(root, fword)

        forbidden_intervals = []
        n = len(word)
        node = root
        for i in range(n):
            j = i
            while j < n and node.children[ord(word[j]) - ord('a')]:
                node = node.children[ord(word[j]) - ord('a')]
                if node.end_of_word:
                    forbidden_intervals.append((i, j))
                    break
                j += 1
            node = root

        forbidden_intervals.append((n, n))
        forbidden_intervals.sort(key=lambda x: x[1])
        max_len = 0
        cur_start = 0
        for start, end in forbidden_intervals:
            cur_length=end - cur_start 
            max_len = max(max_len,cur_length)
            cur_start = max(cur_start,start+1)
        return max_len