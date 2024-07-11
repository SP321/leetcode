class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        d = [{} for _ in range(max(len(x) for x in words) + 1)]
        for w, c in zip(words, costs):
            if w not in d[len(w)]: d[len(w)][w] = c
            elif c < d[len(w)][w]: d[len(w)][w] = c
        
        lengths = [i for i in range(len(d)) if len(d[i])]
        n = len(target)
        
        dp = [10 ** 9] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in lengths:
                if i + j > n: break
                else:
                    try:
                        cost = d[j][target[i:i+j]]
                        if dp[i+j] > dp[i] + cost:
                            dp[i+j] = dp[i] + cost
                    except:
                        pass
        return dp[n] if dp[n] < 10 ** 9 else -1