class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        banned= set()
        st=[]
        
        for i, x in enumerate(s):
            if x not in banned:
                while st and x < st[-1] and c[st[-1]] > 0:
                    banned.remove(st.pop())
                st.append(x)
                banned.add(x)
            c[x] -= 1
        return "".join(st)