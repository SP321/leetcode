class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(len(parent)):
            graph[parent[i]].append(i)
        
        c = Counter()
        ans = 0

        def dfs(node, bitmask):
            nonlocal ans,c
            ans += c[bitmask]
            single_bit = 1
            for i in range(26):
                target_bitmask=bitmask ^ single_bit
                ans += c[target_bitmask]
                single_bit <<= 1

            c[bitmask] += 1
            for child in graph[node]:
                dfs(child, bitmask ^ (1 << (ord(s[child])) - ord("a")))
        
        dfs(0, 0)
        return ans