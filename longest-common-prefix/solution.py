class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=min([len(i) for i in strs])
        for i in range(x):
            ch=strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!=ch:
                    return strs[j][:i]
        return strs[0][:x]