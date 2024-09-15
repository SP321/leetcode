class Vertex:
    def __init__(self):
        self.output = defaultdict(lambda:inf)
        self.link = None         # Suffix link (failure link)
        self.go = {}             # Transitions to child nodes (using dictionaries)

class AhoCorasick:

    def __init__(self, words,costs):
        self.root = Vertex()
        for word, cost in zip(words, costs):
            self.add_string(word, cost)
        self.build_automaton()

    def add_string(self, word,cost):
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.go:
                node.go[ch] = Vertex()
            node = node.go[ch]
        node.output[len(word)] = min(node.output[len(word)],cost)

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
                    if child_node.link!=self.root:
                        for sz,cost in child_node.link.output.items():
                            child_node.output[sz]=min(child_node.output[sz],cost)
    def go(self, node, ch):
        if ch not in node.go:
            tmp=node
            while tmp != self.root and ch not in tmp.go:
                tmp = tmp.link
            node.go[ch]=tmp.go[ch] if ch in tmp.go else self.root
        return node.go[ch]
    
    def iter_matches(self, sentence):
        node = self.root
        for i, ch in enumerate(sentence):
            node = self.go(node, ch)
            
            for sz,cost in node.output.items():
                yield (i, sz, cost)

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        tr = AhoCorasick(words, costs)
        n = len(target)
        dp = [inf] * (n + 1)
        dp[0] = 0

        node = tr.root
        for i,ch in enumerate(target):
            node = tr.go(node, ch)
            for sz,cost in node.output.items():
                dp[i+1] = min(dp[i+1], dp[i - (sz-1)] + cost)

        return dp[n] if dp[n] != inf else -1