class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d=Counter()
        for a,b in zip(messages,senders):
            d[b]+=len(a.split(" "))
        return max(d.keys(),key=lambda x:(d[x],x))
