class Vertex:
    def __init__(self, ln=0):
        self.link = None         # Suffix link (failure link)
        self.go = {}             # Transitions to child nodes (using dictionaries)
        self.ln = ln             # Length of the prefix

class AhoCorasick:

    def __init__(self, words=[]):
        self.root = Vertex()
        for word in words:
            self.add_string(word)
        self.build_automaton()

    def add_string(self, s):
        node = self.root
        for i, ch in enumerate(s):
            if ch not in node.go:
                node.go[ch] = Vertex( i + 1)
            node = node.go[ch]

    def build_automaton(self):
        root = self.root
        queue = deque()
        for node in root.go.values():
            queue.append(node)
            node.link = root

        while queue:
            current_node = queue.popleft()
            for ch, child_node in current_node.go.items():
                queue.append(child_node)
                
                if current_node == self.root:
                    child_node.link = self.root
                else:
                    suffix_node = current_node.link
                    while suffix_node != self.root and ch not in suffix_node.go:
                        suffix_node = suffix_node.link
                    child_node.link = suffix_node.go[ch] if ch in suffix_node.go else self.root

    def go(self, node, ch):
        if ch not in node.go:
            tmp=node
            while tmp != self.root and ch not in tmp.go:
                tmp = tmp.link
            node.go[ch]=tmp.go[ch] if ch in tmp.go else self.root
        return node.go[ch]

    def iter_matches(self, sentence):
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

        node = tr.root        
        for i, ch in enumerate(target):
            node = tr.go(node, ch)
            if node.ln > 0:
                dp[i + 1] = dp[i + 1 - node.ln] + 1

        return dp[-1] if dp[-1]!=inf else -1