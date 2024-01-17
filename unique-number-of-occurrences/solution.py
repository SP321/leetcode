class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x=Counter(arr).values()
        return len(set(x))==len(x)