def create_node():
    return defaultdict(create_node, {
        'fail': None,
        'output': defaultdict(lambda:inf)
    })
KEYSET=set(x for x in create_node())
class AhoCorasick:
    def __init__(self, words, costs):
        self.root = create_node()
        self.build_trie(words, costs)
        self.build_failure_links()

    def build_trie(self, words, costs):
        for word, cost in zip(words, costs):
            self.add(word, cost)

    def add(self, word, cost):
        node = self.root
        for letter in word:
            node = node[letter]
        node['output'][len(word)]=min(node['output'][len(word)],cost)

    def build_failure_links(self):
        root = self.root
        queue = deque()
        for key,node in root.items():
            if key in KEYSET:
                continue
            queue.append(node)
            node['fail'] = root

        while queue:
            current_node = queue.popleft()

            for key, next_node in current_node.items():
                if key in KEYSET:
                    continue
                queue.append(next_node)
                fail_node = current_node['fail']

                while fail_node and key not in fail_node:
                    fail_node = fail_node['fail']

                next_node['fail'] = fail_node[key] if fail_node else root
                if next_node['fail'] is not self.root:
                    for length, cost in next_node['fail']['output'].items():
                        next_node['output'][length] = min(next_node['output'][length],cost)


        root['fail']=root

    def iterstate(self,node,ch):
        while node!=self.root and ch not in node:
            node = node['fail']
        if ch in node:
            node = node[ch]
        else:
            node = self.root
        return node

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        tr = AhoCorasick(words, costs)
        n = len(target)
        dp = [inf] * (n + 1)
        dp[0] = 0
        cur = tr.root

        for i,x in enumerate(target):
            cur = tr.iterstate(cur,x)
            for length, cost in cur['output'].items():
                dp[i+1] = min(dp[i+1], dp[i - (length-1)] + cost)

        return dp[n] if dp[n] != inf else -1