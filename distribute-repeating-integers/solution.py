class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        quantity.sort(reverse=True)
        c = defaultdict(int, Counter(Counter(nums).values()))
        def backtrack(i: int = 0) -> bool:
            if i == len(quantity):
                return True
            
            for x, y in list(c.items()):
                if x >= quantity[i] and y > 0:
                    c[x] -= 1
                    c[x - quantity[i]] += 1
                    if backtrack(i + 1):
                        return True
                    c[x] += 1
                    c[x - quantity[i]] -= 1
            
            return False
        
        return backtrack()