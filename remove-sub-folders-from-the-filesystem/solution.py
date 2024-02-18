class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans, prev = [], "_"
        for x in sorted(folder):
            if not x.startswith(prev+"/"):
                ans.append(x)
                prev = x
        return ans