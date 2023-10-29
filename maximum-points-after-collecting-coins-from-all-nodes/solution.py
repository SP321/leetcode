class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        def dfs(node: int, divide_count: int, parent: int) -> int:
            if (node, divide_count) in memo:
                return memo[(node, divide_count)]
            if divide_count>14:
                return 0
            divided_coins = coins[node] // (2 ** divide_count)
            all_coins = divided_coins - k
            if all_coins<0:
                all_coins-abs(divided_coins - k)
            half_coins = divided_coins // 2
            
            for child in graph[node]:
                if child != parent:
                    child_points = dfs(child, divide_count, node)
                    child_points_divided = dfs(child, divide_count + 1, node)
                    all_coins += child_points
                    half_coins += child_points_divided
                    
            result = max(all_coins, half_coins)
            memo[(node, divide_count)] = result
            return result
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        memo = {}
        return dfs(0, 0, -1)