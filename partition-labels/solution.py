class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = [0]*26
        for i, x in enumerate(s):
            last_index[(ord(x)-ord('a'))]=i
        start = -1
        max_index = 0
        ans = []
        for i, x in enumerate(s):
            max_index = max(max_index, last_index[(ord(x)-ord('a'))])
            if i == max_index:
                ans.append(i - start)
                start = i
        
        return ans