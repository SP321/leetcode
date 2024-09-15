class Vertex:
    def __init__(self, parent=None, ch='$', ln=0):
        self.next = {}           # Transitions to child nodes (dictionary of children)
        self.parent = parent     # Reference to the parent vertex (not an index)
        self.pch = ch            # Character leading to this vertex from its parent
        self.link = None         # Suffix link (failure link)
        self.go = {}             # Transitions to child nodes (using dictionaries)
        self.ln = ln             

class AhoCorasick:

    def __init__(self, words=[]):
        self.root = Vertex()
        for word in words:
            self.add_string(word)

    def add_string(self, word):
        node = self.root
        for i,ch in enumerate(word):
            if ch not in node.next:
                node.next[ch] = Vertex(node, ch, i+1)
            node = node.next[ch]

    def get_link(self, node):
        if node.link is None:
            if node == self.root or node.parent == self.root:
                node.link = self.root
            else:
                node.link = self.go(self.get_link(node.parent), node.pch)
        return node.link

    def go(self, node, ch):
        if ch not in node.go:
            if ch in node.next:
                node.go[ch] = node.next[ch]
            else:
                node.go[ch] = self.root if node == self.root else self.go(self.get_link(node), ch)
        return node.go[ch]

    def iter_matches(self, sentence):
        node = self.root        
        for i, ch in enumerate(sentence):
            node = self.go(node, ch)
            if node.ln > 0:
                yield (i, node.ln)
                
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        tr=AhoCorasick(words)
        n=len(target)
        dp=[inf]*(n+1)
        dp[0]=0
        for i,ln in tr.iter_matches(target):
            dp[i + 1] = dp[i + 1 - ln] + 1

        return dp[-1] if dp[-1]!=inf else -1