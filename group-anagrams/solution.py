class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash(a):
            x=Counter(a)
            return tuple(x[i] for i in "abcdefghijklmnopqrstuvwxyz")
        m=defaultdict(list)
        for i in strs:
            m[hash(i)].append(i)
        return [m[i] for i in m]