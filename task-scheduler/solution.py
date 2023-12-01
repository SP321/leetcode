class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        max_count = max(c.values())
        min_time = (max_count - 1) * (n + 1) + sum([1 for i in c.values() if i==max_count])
    
        return max(min_time, len(tasks))
        