class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        ret = 0
        stack = []
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                ret += 1
            stack.append(d)
        return ret
