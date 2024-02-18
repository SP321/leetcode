class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        next_candle_index=[n]
        prev_candle_index=[-1]
        pref=[0]
        for i,x in enumerate(s):
            if x=='|':
                prev_candle_index.append(i)
                pref.append(pref[-1])
            else:
                prev_candle_index.append(prev_candle_index[-1])
                pref.append(pref[-1]+1)
        for i in range(n-1,-1,-1):
            x=s[i]
            if x=='|':
                next_candle_index.append(i)
            else:
                next_candle_index.append(next_candle_index[-1])
        next_candle_index=next_candle_index[1:][::-1]
        prev_candle_index=prev_candle_index[1:]

        ans=[]
        for st,en in queries:
            a=next_candle_index[st]
            b=prev_candle_index[en]
            c=0
            if a<b and a>=0 and b<n:
                c=pref[b+1]-pref[a]
            ans.append(c)
        return ans