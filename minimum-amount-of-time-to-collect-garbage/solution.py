class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_index=defaultdict(int)
        total=0
        for i,x in enumerate(garbage):
            for j in x:
                total+=1
                last_index[j]=i
        prefix_sum = list(accumulate(travel,initial=0))
        return total + sum(prefix_sum[last_index[c]] for c in 'PGM')